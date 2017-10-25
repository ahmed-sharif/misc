
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

def compute_sequential_mps(lst, from_i=0, mps=None):
    print lst
    n = len(lst)
    if not mps:
        mps = [0 for _ in range(n)]

    if len(mps) < n:
        mps = mps + [0 for _ in range(n - len(mps))]
    elif len(mps) > n::
        mps = mps[:-(len(mps) - n)]


    j = 0
    i = 1
    # for i in range(1, n):
    skip = 0

    if from_i > i:


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
    r = [str(x) for x in mps]            
    print r
    return mps


def compute_mps(lst, from_i=0, mps=None):
    print lst
    n = len(lst)

    j = 0
    i = 1
        
    for i in range(1, n):    

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
    r = [str(x) for x in mps]            
    print r
    return mps


lst = "aabaabaaa"


compute_mps(list(lst))


