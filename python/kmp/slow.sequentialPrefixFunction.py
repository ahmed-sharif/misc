
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java




def compute_sequential_mps(lst, mps=None, j=None, saved_j=None):
    # print "--> start", lst, "saved", saved_j, "mps", mps, "j=",j
    # # print lst
    n = len(lst)
    i = n - 1
    if not mps:
        mps = [0 for _ in range(n)]
        j = 0
        i = 1

    if not saved_j:
        saved_j = [0 for _ in range(n+1)]

    if len(saved_j) < n + 1:

        saved_j.append(0)    

    if len(mps) < n:
        i = len(mps)
        mps.append(0)
        
    elif len(mps) > n:
        mps = mps[:-1]
        ## print "return j =",j
        # # print "return j =",saved_j[n],"mps="
        # return mps, j
        # print "return mps=",mps,"saved_j[n]", saved_j[n], "saved_j",saved_j
        return mps, saved_j[n]

    while i < n:
        # print "comparing i=", i, "j=", j
        if lst[i] == lst[j]:
            mps[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                mps[i] = 0
                i += 1
            else:
                j = mps[j - 1]
    # r = [str(x) for x in mps]            
    # # print r
    saved_j[n] = j
    ## print "return j=",j
    # print "return mps=",mps,"saved_j[n]", saved_j[n], "saved_j",saved_j
    return mps, j


def compute_mps(lst):
    n = len(lst)
    mps = [0 for _ in range(n)]
    j = 0
    i = 1
    while i < n:
        if lst[i] == lst[j]:
            mps[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                mps[i] = 0
                i += 1
            else:
                j = mps[j - 1]
    return mps

saved_j = [0]

lst = "aabaabaaa"

lst = []

n = int(raw_input().strip())
res = None
j = None
for _ in range(n):
    inp = raw_input().strip().split()

    if inp[0] == '+':
        lst.append(inp[1])
        # res = compute_mps(lst, res)

        res, j = compute_sequential_mps(lst, res, j, saved_j)
        # res = compute_mps(lst)
        print res[-1]
    else:
        lst = lst[:-1]
        if lst:
            # res = compute_mps(lst, res)
            # res = compute_mps(lst)
            res, j = compute_sequential_mps(lst, res, j, saved_j)
            print res[-1]
        else:
            if res:
                res = res[:-1]
            # print lst
            print 0


# compute_mps(list(lst))