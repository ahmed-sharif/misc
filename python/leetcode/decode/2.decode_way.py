
"""

1   2   3   4   2   1


f(1) + f(2   3   4   2   1) + f(12) + f(3   4   2   1)
       f(2) + f(3   4   2   1)
       f(23) + f(4 2 1) 
"""

total = 0

dp = {}
from collections import deque

def decode_way(item):
    
    global total
    global dp

    if item in dp:
        print "\t\t\t", item
        return dp[item]

    print item

    total += 1

    if len(item) == 1:
        return [deque([item])]
        return 1

    if len(item) == 2:
        if int(item) <= 26:
            return [deque([item]), deque([item[0], item[1]])]
            return 2
        else:
            return [deque([item[0], item[1]])]
            return 1

    r1 = decode_way(item[1:])

    for i in r1:
        # i.insert(0, item[0])
        i.appendleft(item[0])

    r2 = []
    if int(item[:2]) <= 26:
        r2 = decode_way(item[2:])

        for i in r2:
            # i.insert(0, item[:2])
            i.appendleft(item[:2])

    result = r1 + r2
    dp[item] = result
    return result 
"""
1   2   3
12  3
1   23
"""

#print decode_way("123")

item = "123412341231242342341212341234123124234234121234123412312423423412"
item = "1234123412312423423412123"
item = ""
item = "12111"
print len(item)
n = decode_way(item)
print 'r=',len(n)
print len(item)
# print n
# print decode_way("2")
#print decode_way("1234")

print total



"""
1,   2   1   2   1   2

1,   2,    1   2   1   2
1,   2,    1,   2   1   2

1,   2,    12,   1   2

1,   21,   2   1   2


12,  1   2   1   2     
"""

