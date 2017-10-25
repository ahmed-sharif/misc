


def getRow(A):
    res = [0 for i in xrange(A+1)]
    
    for i in range(1, A + 2):
        res[0] = 1
        res[i-1] = 1
        print res
        #for j in range(1, i-1):
        for j in range(i-2, 0, -1):    
            res[j] = res[j] + res[j - 1]

    return res


print getRow(5)