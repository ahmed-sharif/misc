#!/bin/python

n,p = raw_input().strip().split()
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split())
# your code goes here


used = {}
b_used = {}

total_buttons = 0


max_used_for_cost = {}

for cost in a:
    minimum_buttons_required = cost / p
    if cost % p != 0:
        minimum_buttons_required += 1
    ct = 0
    print "trying to get cost for", cost,'min_required=',minimum_buttons_required
    if cost in max_used_for_cost:
        minimum_buttons_required = max_used_for_cost[cost] + 1
        while True:
            print "ctccc=",ct,"minimum_buttons_required=",minimum_buttons_required, used
            ct += 1
            if minimum_buttons_required in used:
                minimum_buttons_required += 1
                continue
            used[minimum_buttons_required] = True    
            total_buttons += minimum_buttons_required
            
            max_used_for_cost[cost] = minimum_buttons_required
            break
        print ct,max_used_for_cost
        
    else:
        while True:
            print "ct=",ct,"minimum_buttons_required=",minimum_buttons_required, used
            ct += 1
            if minimum_buttons_required in used:
                minimum_buttons_required += 1
                continue
            used[minimum_buttons_required] = True    
            total_buttons += minimum_buttons_required
            
            max_used_for_cost[cost] = minimum_buttons_required
            break
        print ct,max_used_for_cost
print total_buttons        
        
            
            
    
        

