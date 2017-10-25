# Enter your code here. Read input from STDIN. Print output to STDOUT



M, N, R = raw_input().strip().split()

M = int(M)
N = int(N)
R = int(R)

# M rows
# N cols

input_ = []
cache = []
rotation_max = []
for _ in xrange(M):
    a_temp = map(int,raw_input().strip().split(' '))
    
    input_.append(a_temp)
    # input_.append([None] * N)
    cache.append([None] * N)
    rotation_max.append([None] * N)

def get_rotation_max(input_):
    nr = len(input_)
    nc = len(input_[0])
    i = 0
    j = 0
    while i < (nr + 1) / 2 and j < (nc + 1) / 2:
        
        ml = (nc - i * 2) * 2
        ml += (nr - i * 2 - 2) * 2
        #

        for k in range(j, nc - i):
            #input_[i][k] = "%2d%2d" % (i, k)
            #input_[nr-1-i][k] = "%2d%2d" % (nr-1-i, k)

            rotation_max[i][k] = ml
            rotation_max[nr-1-i][k] = ml
        for sr in range(i+1, nr-1-i):
            #input_[sr][j] = "XXXX"
            #input_[sr][nc - 1 - j] = "XXXX"

            rotation_max[sr][j] = ml
            rotation_max[sr][nc - 1 - j] = ml

        i += 1
        j += 1

def _find_pos(i, j):
    return cache[i][j]
    
def _precompute(input_):
    sr = 1
    er = len(input_)        
    for t in range(len(input_[0])/2):
        for r in range(sr, er):
            cache[r][t] = (r-1, t)
            # L
        sr += 1
        er -= 1

    sc = 0
    ec = len(input_[0]) - 1
        
    for r in range(len(input_)/2):
        for c in range(sc, ec):
            cache[r][c] = (r, c+1)
            # T
        sc += 1
        ec -= 1

    sr = 0
    er = len(input_)-1

    for t in range(len(input_[0])-1,len(input_[0])/2-1, -1):
        for r in range(sr, er):
            # R            
            cache[r][t] = (r+1, t)
        sr += 1
        er -= 1 
    
    if(len(input_)%2 == 0):
        er = len(input_)/2 - 1
    else:
        er = len(input_)/2
    
    sc = 1
    ec = len(input_[0])
        
    for r in range(len(input_)-1, er, -1):
        for c in range(sc, ec):
            cache[r][c] = (r, c-1)
            # B
        sc += 1
        ec -= 1

_precompute(input_)
"""
for i in range(len(input_)):
    for j in range(len(input_[0])):
        print "%2d" % input_[i][j],
    print
print "-----------"
"""
# find_rotation_max(input_)
get_rotation_max(input_)
"""
print "-------"
for i in range(len(input_)):
    for j in range(len(input_[0])):
        print "%3d" % rotation_max[i][j],
    print

import sys
sys.exit(0)
"""
for i in range(len(input_)):
    for j in range(len(input_[0])):
        ii=i
        jj=j

        r_m = rotation_max[i][j]
        no_of_rotation_required = R % r_m
        # no_of_rotation_required = R
        r = i
        c = j
        for rot in range(no_of_rotation_required):
            #r,c = _find_pos(ii, jj)
            r,c = cache[ii][jj]
            ii=r
            jj=c
        # print i,j, "=", r,c, "---",
        print "%d" % input_[r][c],
    print
    
