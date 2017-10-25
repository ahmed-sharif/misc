# import time

import copy
def manually_generate(item, n):
    temp = [0 for _ in range(len(item))]
    for x in range(n):
        for i in range(len(item)-1):
            temp[i]= item[i] ^ item[i+1]

        temp[len(item)-1] = item[len(item)-1] ^ item[0]
        # print temp
        # p_item(temp)
        item = copy.copy(temp)
    return temp


items = [1,2,3,4,5,6,7,8,9]
print "original", items
for i in range(1, 19):
    t = copy.copy(items)
    print i, "     =", manually_generate(t, i)


print "--------"
items = [1,2,3,4,5,6]
print "original", items
for i in range(1, 19):
    t = copy.copy(items)
    print i, "     =", manually_generate(t, i)    
