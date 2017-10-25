#!/bin/python


"""


-
-




"""


import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]



# found = False

if v2 >= v1:
    print "NO"
else:
    i = 1
    while True:
        x1_pos = x1 + v1 * i
        x2_pos = x2 + v2 * i
        if x1_pos == x2_pos:
            print "YES"
            break
        if x1_pos > x2_pos:
            print "NO"
            break
        i += 1

