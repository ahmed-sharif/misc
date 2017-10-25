#!/bin/python
from fractions import gcd
import sys


n = int(raw_input().strip())
total = 0
for i in range(2, n):
    max_multiple_for_i = n / i
    """    
    for t in range(i+1, max_multiple_for_i+1):
        if gcd(i, t) == 1:
            print i, t
    """
    total_number_inbetween = max_multiple_for_i - i
    to_subtract = (max_multiple_for_i / i) - 1
    total_eligible = total_number_inbetween - to_subtract
    if i%2 == 0 and i!= 2:
        total_eligible = total_eligible - (total_number_inbetween / 2 - to_subtract)
    if total_eligible <= 0:
        break
    print "total for",i,"=",total_eligible
    total += total_eligible
print total

