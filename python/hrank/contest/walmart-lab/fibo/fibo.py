
arr = [0, 1]

def get_fibo(n):
    ln = len(arr)
    if n < ln:
        return arr[n]

    for i in range(ln, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]

#for i in range(11):
#    print get_fibo(i)


n = 4

for i in xrange(n, 0, -1):
    for j in xrange(i):
        for k in xrange(n-i+1):
            print k+j+1,",",
        print