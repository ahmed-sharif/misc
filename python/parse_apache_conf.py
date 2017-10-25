#!/usr/bin/env python
import re

filename = "apache_conf.txt"

regex = re.compile(r"(<Directory\s*(\S*)>\s*Options\s*\w*\s*FollowSymLinks.*?</Directory>)", re.DOTALL)

with open(filename) as fd:
    filecontent = fd.read()
    for m in regex.finditer(filecontent):
        print m
        print m.start(), m.end()
        print m.group(2)
        print ""



