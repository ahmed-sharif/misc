import sys
import json
import time
from threading import Thread, Lock

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
    # amf.send_metrics(host="ltx1-admin01.prod.linkedin.com", appname="Unhealthhostspercentage", metrics=metrics)
    print (metric_dict)
    '''print_row(h.group, h.site, h.count_inops_devices(),
              h.count_obhc_hosts(), h.count_unhealthy_hosts(),
              "({0:>5.2f}%)".format(h.unhealthy_percent()))'''

# TODO: refactor everything below :-(


class Health(object):
    def __init__(self):
        # TODO: remove poor-man's non-pythonic memoization hacks
        self._inops_device_count   = None
        self._obhc_host_list       = None
        self._obhc_host_names      = None
        self._obhc_unhealthy_hosts = None


    def unhealthy_percent(self):
        return float(self.count_unhealthy_hosts()) / self.count_obhc_hosts() * 100.0


class FleetHealth(Health):
    """Represents health of multiple fabric groups."""
    def __init__(self):
        Health.__init__(self)

        self.group = ""
        self.site = "Sum"  # hack to enable print_health (refactor?)
        self.fabric_group_healths = []


    def append_fabric_group_health(self, fabric_group_health):
        self.fabric_group_healths.append(fabric_group_health)

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

        # self.group, self.site = fabric.name.split("-", 2)
        self.group, self.site = fabric.split("-", 2)

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

        self._inops_device_count = 3000

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

        self._obhc_host_list = json.loads(open("allh").read())
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
        if self._obhc_unhealthy_hosts is not None:
            return self._obhc_unhealthy_hosts

        self._obhc_unhealthy_hosts = []

        self._obhc_unhealthy_hosts = json.loads(open("allh").read())

        return self._obhc_unhealthy_hosts


def sorted_fabric_list():
    # fabrics = all_fabrics()
    fabrics = ['prod-lva1', 'prod-ltx1', 'prod-lor1', 'ei-ltx1', 'ei-lca1']
    # fabrics.sort(key=lambda x: x.name)
    return fabrics


def process_fabric(fabric):
    fabric_health = FabricHealth(fabric)

    results_lock.acquire()
    results_list.append(fabric_health)
    results_lock.release()


def main():
    while True:
        print "Started Running"
        results_list[:] = []
        start_time = time.time()
        threads = []
        for fabric in sorted_fabric_list():

            thread = Thread(target=process_fabric, args=(fabric,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print_header()

        last_fabric_group_health = None
        fleet_health = FleetHealth()
        print len(results_list)
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
	        time.sleep(1)
if __name__ == "__main__":
    sys.exit(main())

# vim: set ts=4 sw=4 sts=4 tw=79 ft=python
