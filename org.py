#!/export/content/linkedin/bin/deployment-tools.pex

#!/bin/bash
''''true
export PEX_FORCE_LOCAL=true
export PEX_PYTHON=/export/apps/python/2.7/bin/python
export PEX_PATH=/export/content/linkedin/bin/lipy-inops.pex
exec /export/content/linkedin/bin/track-tools-cli.pex $0 $@
'''

# from __future__ import division

import json
import urllib3
import time
# from collections import Counter
from threading import Thread, Lock

import linkedin.inops as inops
from linkedin.inops.client import Client
from linkedin.fabric import all_fabrics
from linkedin.amfclient import ApiClient
amf=ApiClient('prod-lva1')


inops_client = Client()

# TODO: remove this and actually validate SSL certificates
urllib3.disable_warnings()

# Base API URL, which will be fed to .format() with a lipy-fabric Fabric
# object. This is an ATS/IPVS endpoint which is accessible anywhere in biz.
#
# Direct queries against the server are possible, but that would require
# changes elsewhere, and is not recommended due to network ACLs.
OBHC_API_URL = "https://obhc-api{fabric.subdomain_name}/{fabric.name}/api/v1"

# This causes the API to always return responses compliant with the JSON API
# specification. Some API endpoints require this header, but it should always
# be used regardless.
OBHC_API_HEADERS = {
    "Content-Type": "application/vnd.api+json"
}

# To retrieve host health information from OBHC, we currently have to go
# through a few steps:
#
# 1. Query OBHC for a list of all hosts it has seen.
# 2. Query OBHC for the state of host health checks for each host.
#
# Queries for check state can be batched such that we retrieve checks for
# multiple hosts at once. While OBHC is extremely fast to respond to most
# queries, ATS will often return errors on large queries (either due to the
# large number of host names in the query parameters, or due to timeouts). To
# work around this, queries are chunked. 500 is known to work everywhere.
OBHC_API_FILTER_MAX = 500

# At the time of writing, these are the checks that LID looks at for
# deployment, and so this represents the "health" of the fleet.
OBHC_CHECKS = ["heartbeat", "host_diskspace", "host_inodes", "host_salt"]

# Production states to use when getting a host count from InOps. In general,
# this should be anything which *could* report to OBHC. Since InOps does not
# have a concept of fabrics or use after imaging, and hosts (especially VMs)
# have been known to stay in the wrong state after creation, all we can do is
# approximate and guess.
# https://docs.google.com/spreadsheets/d/10dZ_u3mmuX5AdWam4IbmqJ6wXLnWnWOgiN8VCqFGqY0/edit#gid=0
VALID_INOPS_PRODUCTION_STATES = [
    "Pre-Production",
    "Production",
    "Non-Production"
]

# These are the class names which are likely to be running obhc-agent, and
# could be considered a member of the "fleet" on which we are reporting.
VALID_INOPS_CLASS_NAMES = [
    "Device.Server.",
    "Device.ServerModule.",
    "Device.VM."
]

# Health data is aggregated per fabric, will all fabrics processing in
# parallel. Those go into the below list and are then sorted and placed into a
# tree structure (see notes near the bottom of the file for why and suggestions
# on changing this process). The lock is probably not necessary because of the
# GIL, but it is used anyway.
results_lock = Lock()
results_list = []


def print_row(*args):
    print "{:>5} {:>5} {:>10} {:>10} {:>6}{:>9}".format(*args)


def print_separator(character="="):
    print character * 49


def print_header():
    print_row("Group", "Site", "Hosts", "Reporting", "", "Unhealthy")
    print_separator()


def print_health(h):

    # Change the hostname and appname and metric name to required values
    metrics=[]
    metric_dict = dict(
                metric="metric_{0}".format(h.site), time=int(time.time()),
                value=h.unhealthy_percent(), metric_type='GAUGE'
            )
    metrics.append(metric_dict)
    amf.send_metrics(host="ltx1-admin01.prod.linkedin.com", appname="Unhealthhostspercentage", metrics=metrics)
    #print (metric_dict)
    '''print_row(h.group, h.site, h.count_inops_devices(),
              h.count_obhc_hosts(), h.count_unhealthy_hosts(),
              "({0:>5.2f}%)".format(h.unhealthy_percent()))'''

# TODO: refactor everything below :-(


class Health(object):
    """Generic class for accessing statistics regarding host health.

    todo:: This is highly specific to OBHC and InOps data. Make this class (and
    all classes which inherit it) more generic.
    """


    def __init__(self):
        # TODO: remove poor-man's non-pythonic memoization hacks
        self._inops_device_count   = None
        self._obhc_host_list       = None
        self._obhc_host_names      = None
        self._obhc_unhealthy_hosts = None


    def unhealthy_percent(self):
        """Return the percent of reporting hosts (hosts which are in OBHC's
        database) which have a failed host health check.

        note:: This does not take into account the number of hosts as reported
        by inOps. If this is desired, inOps will need to be queried for a list
        of host names and that list will need to be compared with OBHC's list,
        missing hosts identified, and other inconsistencies reconciled.
        Otherwise, data will be even more approximate than it already is.
        """
        return float(self.count_unhealthy_hosts()) / self.count_obhc_hosts() * 100.0


    def count_obhc_hosts(self):
        raise NotImplementedError


    def count_unhealthy_hosts(self):
        raise NotImplementedError


    def count_inops_devices(self):
        raise NotImplementedError


    def obhc_host_list(self):
        raise NotImplementedError


    def obhc_host_names(self):
        raise NotImplementedError


    def obhc_unhealthy_hosts(self):
        raise NotImplementedError


class FleetHealth(Health):
    """Represents health of multiple fabric groups."""


    def __init__(self):
        Health.__init__(self)

        self.group = ""
        self.site = "Sum"  # hack to enable print_health (refactor?)
        self.fabric_group_healths = []


    def append_fabric_group_health(self, fabric_group_health):
        self.fabric_group_healths.append(fabric_group_health)

        # TODO: remove poor-man's non-pythonic memoization hacks
        self._inops_device_count   = None


    def count_inops_devices(self):
        if self._inops_device_count is not None:
            return self._inops_device_count

        self._inops_device_count = 0

        for group in self.fabric_group_healths:
            self._inops_device_count += group.count_inops_devices()

        return self._inops_device_count


    def count_obhc_hosts(self):
        count = 0

        for group in self.fabric_group_healths:
            count += group.count_obhc_hosts()

        return count


    def count_unhealthy_hosts(self):
        count = 0

        for group in self.fabric_group_healths:
            count += group.count_unhealthy_hosts()

        return count


class FabricGroupHealth(Health):
    """Represents health of multiple fabrics within one fabric group (e.g.,
    prod fabrics: prod-lva1, prod-ltx1, etc.).

    Information shown here is always gathered from children (FabricHealth
    objects).
    """


    def __init__(self, name, site="Sum"):
        Health.__init__(self)

        self.group = name
        self.site = site
        self.fabric_healths = []


    def append_fabric_health(self, fabric_health):
        self.fabric_healths.append(fabric_health)

        # TODO: remove poor-man's non-pythonic memoization hacks
        self._inops_device_count   = None


    def count_inops_devices(self):
        if self._inops_device_count is not None:
            return self._inops_device_count

        self._inops_device_count = 0

        for health in self.fabric_healths:
            self._inops_device_count += health.count_inops_devices()

        return self._inops_device_count


    def count_obhc_hosts(self):
        count = 0

        for health in self.fabric_healths:
            count += health.count_obhc_hosts()

        return count


    def count_unhealthy_hosts(self):
        count = 0

        for health in self.fabric_healths:
            count += health.count_unhealthy_hosts()

        return count


class FabricHealth(Health):
    """Represents health of hosts within one fabric.

    Actual API calls to remote services (OBHC, InOps) are implemented within
    this class.
    """


    def __init__(self, fabric):
        Health.__init__(self)

        self.fabric = fabric

        self.group, self.site = fabric.name.split("-", 2)

        # For now, populate these as soon as we're instantiated.
        self.count_inops_devices()
        self.count_unhealthy_hosts()


    def count_obhc_hosts(self):
        """Count the unique host names that are in OBHC's database for this
        fabric.

        :returns: number of unique host names seen by OBHC
        :rtype: int
        """
        return len(self.obhc_host_names())


    def count_unhealthy_hosts(self):
        """Count the number of hosts which have at least one failed host health
        check, according to OBHC.

        :returns: number of hosts with at least one failed host health check
        :rtype: int
        """
        return len(self.obhc_unhealthy_hosts())


    def count_inops_devices(self):

        if self._inops_device_count is not None:
            return self._inops_device_count

        self._inops_device_count = 0

        for production_state in VALID_INOPS_PRODUCTION_STATES:
            for class_name in VALID_INOPS_CLASS_NAMES:
                self._inops_device_count += inops_client.count(
                    inops.Device,
                    production_state=production_state,
                    site=self.site,
                    class_name=class_name,
                    name_like="%{0}".format(
                        self.fabric.subdomain_name))

        return self._inops_device_count


    def obhc_host_list(self):
        """Get the hosts seen by OBHC in this fabric. Data is structured
        according to the OBHC API specification. The `data` field from the
        response is returned here.`

        :returns: hosts seen by OBHC
        :rtype: list
        """
        if self._obhc_host_list is not None:
            return self._obhc_host_list

        http = urllib3.PoolManager()  # XXX should this be here?

        url = OBHC_API_URL + "/hosts"

        request = http.request(
            "GET", url.format(fabric=self.fabric), headers=OBHC_API_HEADERS)

        response_data = request.data
        response = json.loads(response_data.decode("utf-8"))

        self._obhc_host_list = response["data"]

        return self._obhc_host_list


    def obhc_host_names(self):
        """Returns a list of unique host names in the OBHC database.

        :returns: unique host names
        :rtype: list
        """


        if self._obhc_host_names is not None:
            return self._obhc_host_names

        self._obhc_host_names = list(set(
            [host["id"] for host in self.obhc_host_list()]))

        return self._obhc_host_names


    def obhc_unhealthy_hosts(self):
        """Get a list of all hosts that are unhealthy according to OBHC. Data
        is structured according to the OBHC API specification, and includes
        check results. The list includes the entire `host` resoure object for
        each host with a failed health check.

        Checks used are, at the time of writing, hard-coded to be the same as
        those used by LID:

        - heartbeat
        - host_diskspace
        - host_inodes
        - host_salt

        :returns: list of host with failed host health check
        :rtype: list
        """


        if self._obhc_unhealthy_hosts is not None:
            return self._obhc_unhealthy_hosts

        http = urllib3.PoolManager()  # XXX should this be here?
        chunks = [
            self.obhc_host_names()[x:x+OBHC_API_FILTER_MAX] for x in xrange(
                0, len(self.obhc_host_names()), OBHC_API_FILTER_MAX)
        ]

        self._obhc_unhealthy_hosts = []

        for chunk in chunks:
            fields = {
                "filter[name]": ",".join(chunk),
                "filter[check]": ",".join(OBHC_CHECKS)
            }

            url = OBHC_API_URL + "/hosts"

            request = http.request(
                "GET", url.format(fabric=self.fabric),
                headers=OBHC_API_HEADERS,
                fields=fields)

            response_data = request.data
            response = json.loads(response_data.decode("utf-8"))

            # TODO: this can probably be much more pythonic
            for host in response["data"]:
                if not False in host["attributes"]["checks"].values():
                    continue
                self._obhc_unhealthy_hosts.append(host)

        return self._obhc_unhealthy_hosts


def sorted_fabric_list():
    fabrics = all_fabrics()
    fabrics.sort(key=lambda x: x.name)

    return fabrics


def process_fabric(fabric):
    fabric_health = FabricHealth(fabric)

    results_lock.acquire()
    results_list.append(fabric_health)
    results_lock.release()


def main():
    # TODO: all of this (below) could be wrapped into FleetHealth and then just
    # iterate through the data at the end, rather than building it as we
    # output.  For the moment, I have avoided doing so because I dislike the
    # pattern of building threads into places that are likely to become
    # libraries.


    # Each fabric's data is collected by separate threads. This is because some
    # of the requests take a long time to complete, and i/o bounding may be
    # limited to a particular fabric. A few pieces here have limited utility
    # due to GIL, but it is still faster overall.
    while True:
        print "Started Running"
        start_time = time.time()
        threads = []
        for fabric in sorted_fabric_list():
            # TODO: no hard-coded filtering. Instead, maybe we could find out where
            # obhc-server is running (via lipy-fabric), and query those
            # fabrics/sites which have obhc-server.
            if "lit" in fabric.name:
                continue

            thread = Thread(target=process_fabric, args=(fabric,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Sort results by fabric name, then iterate through and print a table.

        results_list.sort(key=lambda x: x.fabric.name)

        print_header()

        last_fabric_group_health = None
        fleet_health = FleetHealth()

        for result in results_list:
            if last_fabric_group_health is None:
                last_fabric_group_health = FabricGroupHealth(result.group)

            elif last_fabric_group_health.group != result.group:
                print_health(last_fabric_group_health)

                print_separator("-")

                fleet_health.append_fabric_group_health(last_fabric_group_health)
                last_fabric_group_health = FabricGroupHealth(result.group)

            last_fabric_group_health.append_fabric_health(result)

            print_health(result)

        fleet_health.append_fabric_group_health(last_fabric_group_health)

        print_health(last_fabric_group_health)

        print_separator("=")

        print_health(fleet_health)
        end_time = int(time.time())
        if (int(end_time - start_time) < 61):
            #time.sleep(61 - int(end_time - start_time))
            #print("Sleeping for {0}".format(301 - int(end_time - start_time)))
	    time.sleep(300 - int(end_time - start_time))
if __name__ == "__main__":
    sys.exit(main())

# vim: set ts=4 sw=4 sts=4 tw=79 ft=python
