#!/bin/python


def frequency_atleast_two(bugs_count):
    items_less_than_two = [b for b in bugs_count if bugs_count[b] == 1 and b != '_']
    return len(items_less_than_two) == 0


def already_happy(bugs):
    if len(bugs) == 1:
        return False
    
    # check first 2 item
    if bugs[0] != bugs[1]:
        return False

    # check last 2 item
    if bugs[len(bugs) - 1] != bugs[len(bugs) - 2]:
        return False


    for i in range(1, len(bugs) - 1):
        if bugs[i] != bugs[i - 1] and bugs[i] != bugs[i + 1]:
            return False

    return True


Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b_count = {}
    b = raw_input().strip()
    for char in b:
        b_count[char] = b_count.get(char, 0) + 1
    no_of_underscore = b_count.get('_', 0)
    # if there is no underscore
    # check if they are already happy 
    # print b_count   
    if no_of_underscore == 0:
        if already_happy(b):
            print "YES"
        else:
            print "NO"
    # if there is only underscore but no bugs
    # then there is no unhappy bugs
    elif len(b_count.keys()) == 1:
        print "YES"
    # if there is underscore
    # check if all bugs have count of at least 2
    else:
        if frequency_atleast_two(b_count):
            print "YES"
        else:
            print "NO"

