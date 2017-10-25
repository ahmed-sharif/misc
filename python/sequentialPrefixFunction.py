


def sequential_prefix_function(lst):
    n = len(lst)

    for k in range(n - 1, 0, -1):
        print "checking", k
        for x in range(k):
            print "\tchecking", x, "==", n-k+x
            lst[x] == lst[n-k+x]




lst = [1,2,3,4,5,6]


sequential_prefix_function(lst)