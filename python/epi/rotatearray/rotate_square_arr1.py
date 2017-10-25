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


size = 4

for i in range(size/2):
    print i
    for j in range(i, size-i-1):
        print "\t",j
        temp = arr[i][j]
        arr[i][j] = arr[i+j][size-1-i]
        print arr[i][j] , i+j, size-1-i        
        arr[i+j][size-1-i] = arr[size-1-i][size-1-j]
        arr[size-1-i][size-1-j] = arr[size-1-j][i]
        arr[size-1-j][i] = temp

        for k in arr:
            print k
        print "----"
        #break
    #break


