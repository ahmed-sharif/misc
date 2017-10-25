
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

def compute_mps(lst, mps, saved_j,running_total):
    print "current", lst[:running_total]

    if saved_j[running_total] != -1:
        print "before saved", saved_j
        saved_j[running_total + 1] = -1
        print "after saved", saved_j
        return

    n = running_total
    j = saved_j[n - 1]
    if running_total == 1:
        i = 1
        j = 0
    else:
        i = n - 1


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
    print "just saved", saved_j


n = int(raw_input().strip())
mps = [-1 for _ in range(n)]
tobeprinted = [-1 for _ in range(n)]
lst = [-1 for _ in range(n)]
saved_j = [-1 for _ in range(n+1)]

running_total = 0

mps[0] = 0
res = None
j = None
for xx in range(n):
    
    inp = raw_input().strip().split()

    if inp[0] == '+':
        lst[running_total] = int(inp[1])
        running_total += 1 
        
        
        compute_mps(lst, mps, saved_j, running_total)
        
        tobeprinted[xx] = mps[running_total-1]
        
    else:
        
        running_total -= 1

        compute_mps(lst, mps, saved_j,running_total)
        
        tobeprinted[xx] = mps[running_total-1]
tobeprinted = [str(i) for i in tobeprinted]        
print "\n".join(tobeprinted)
