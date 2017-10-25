
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java


def compute_sequential_mps(lst, mps=None, j=None, saved_j=None, running_total=0):
    # print "--> start", lst, "saved", saved_j, "mps", mps, "j=",j
    # # print lst
    n = len(lst)
    i = n - 1
    
    n = running_total


    if not mps:
        mps = [0 for _ in range(n)]
        j = 0
        i = 1

    i = running_total
    if running_total <= 1:
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
        return mps, saved_j[n]

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
    
    saved_j[n] = j
    
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
    


n = int(raw_input().strip())
saved_j = [0 for _ in range(n)]
lst = [0 for _ in range(n)]
res = [0 for _ in range(n)]
j = None
running_total = 0

for _ in range(n):
    inp = raw_input().strip().split()
    if inp[0] == '+':
        lst[running_total] = inp[1]
        running_total += 1
        res, j = compute_sequential_mps(lst, res, j, saved_j, running_total)
        print res[running_total - 1]
    else:
        running_total -= 1
        if running_total == 0:
            print 0
        else:
            res, j = compute_sequential_mps(lst, res, j, saved_j, running_total)
            print res[running_total - 1]
