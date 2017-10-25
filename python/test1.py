import copy



def p_item(itm,n=100):
    """
    for i in itm:
        print "%-5s" % bin(i)[2:],
    print
    """
    start = 0
    for i in itm:
        if start == n:
            break
        print "%-5d" % i,
        start = start + 1
    print


item = [16, 72, 15, 38]
item = [1, 2, 5, 5,13,9]
item = [6, 7, 1, 3]
# item = [1, 2, 5, 5,13]
# print item
p_item(item)
temp = [0 for _ in range(len(item))]
for x in range(8):
    for i in range(len(item)-1):
        temp[i]= item[i] ^ item[i+1]

    temp[len(item)-1] = item[len(item)-1] ^ item[0]
    # print temp
    p_item(temp)
    item = copy.copy(temp)

"""
a0            a1            a2            a3            a4              a5

a0^a1         a1^a2         a2^a3         a3^a4         a4^a5           a5^a0

a0^a1^a1^a2   a1^a2^a2^a3   a2^a3^a3^a4   a3^a4^a4^a5   a4^a5^a5^a0     a5^a0^a0^a1


a0^a1^a1^a2^a1^a2^a2^a3   a1^a2^a2^a3^a2^a3^a3^a4  a2^a3^a3^a4^a3^a4^a4^a5  a3^a4^a4^a5^a4^a5^a5^a0    a5^a0^a0^a1^a0^a1^a1^a2

1 3 3 1                     1 3 3 1

a0^a1^a1^a2^a1^a2^a2^a3^a1^a2^a2^a3^a2^a3^a3^a4     a1^a2^a2^a3^a2^a3^a3^a4^a2^a3^a3^a4^a3^a4^a4^a5     a2^a3^a3^a4^a3^a4^a4^a5^a3^a4^a4^a5^a4^a5^a5^a0   a3^a4^a4^a5^a4^a5^a5^a0^a5^a0^a0^a1^a0^a1^a1^a2
1   4   6   4   1                                   1   4   6   4   1


a0                          a1                          a2                          a3  
a0^a1                       a1^a2                       a2^a3                       a3^a0
a0^a1^a1^a2                 a1^a2^a2^a3                 a2^a3^a3^a0                 a3^a0^a0^a1
a0^a1^a1^a2^a1^a2^a2^a3     a1^a2^a2^a3^a2^a3^a3^a0     a2^a3^a3^a0^a3^a0^a0^a1     a3^a0^a0^a1^a0^a1^a1^a2

1(a0)3(a1)3(a2)1(a3)
1 3 3 1                     1 3 3 1                     1 3 3 1                     1 3 3 1
1 4 6 4 1
"""







