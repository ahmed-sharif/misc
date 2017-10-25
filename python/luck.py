#!/bin/python

"""
-
-
"""
# print l
import sys

contensts = []
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]

for _ in range(n):
    lck, imp = raw_input().strip().split(' ')
    lck, imp = [int(lck), int(imp)]
    contensts.append((lck, imp))

importants = [x for x in contensts if x[1] == 1]
un_important_total = sum(x[0] for x in contensts if x[1] == 0)

# print contensts
# print importants
# print un_important_total

importants.sort(key= lambda y: y[0])



# print importants

# print importants, k
total_to_subtract = 0
total_win = 0
if k < len(importants):
    total_win = len(importants) - k
    total_to_subtract = sum(x[0] for x in importants[:total_win])

# print total_win
# print "total_to_subtract=", total_to_subtract
total_to_add = sum(x[0] for x in importants[total_win:])
# print "total_to_add=",total_to_add
# print "un_important_total=", un_important_total
print total_to_add + un_important_total - total_to_subtract


