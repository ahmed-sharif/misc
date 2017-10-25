"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16


i=0 to size/2
    j=i to size-1-i
        i,    j
        i+j,    size-1-i
        size-1-i,   size-1-j
        size-1-j,  i

"""

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

arr = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36]
]


size = 6

for i in range(size/2):
    print "i=",i
    print "----"
    for j in range(i, size-i-1):
        print "----"
        print i, j
        print i + j - i, size - 1 - i
        print size - 1 - i, size - 1 - j
        print size - 1 - j, i

        t1 = arr[i][j]
        t2 = arr[j][size - 1 - i]
        t3 = arr[size - 1 - i][size - 1 - j]
        t4 = arr[size - 1 - j][i]

        arr[i][j] = t2
        arr[j][size - 1 - i] = t3
        arr[size - 1 - i][size - 1 - j] = t4
        arr[size - 1 - j][i] = t1
        

        #for k in arr:
        #    print k
        
        #break
    #break



for k in arr:
    print k