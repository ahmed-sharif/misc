
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

def compute_mps(lst, mps, saved_j,running_total):
    # # print lst
    n = len(lst)
    # mps = [0 for _ in range(n)]
    j = 0
    i = 1

    if saved_j[running_total] != -1:
        #print "returning, saved_j[running_total]=", saved_j[running_total], ",running_total=",running_total
        # saved_j[running_total] = -1
        saved_j[running_total + 1] = -1

        return

    n = running_total
    j = saved_j[n - 1]
    if running_total == 1:
        i = 1
        j = 0
    else:
        i = n - 1

    #print i, j    
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
    # return mps

lst = "aabaabaaa"

# lst = []

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
        #print "adding"
        #print "in  = ", lst
        #print "out = ", mps
        # print mps[running_total-1]
        tobeprinted[xx] = mps[running_total-1]
        #print "saved=", saved_j
    else:
        
        running_total -= 1

        compute_mps(lst, mps, saved_j,running_total)
        #print "removing"
        #print "in  = ", lst
        #print "out = ", mps
        # print mps[running_total-1]
        tobeprinted[xx] = mps[running_total-1]
tobeprinted = [str(i) for i in tobeprinted]        
print "\n".join(tobeprinted)
        #print "saved=", saved_j
    # print    
    