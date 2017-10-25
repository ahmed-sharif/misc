# Enter your code here. Read input from STDIN. Print output to STDOUT
import pprint
import sys


M = int(sys.argv[1])
N = int(sys.argv[2])

# M rows
# N cols

input_ = []
cache = []
rotation_max = []
for _ in xrange(M):
    input_.append(['9999'] * N)
    cache.append([None] * N)
    rotation_max.append([99] * N)

#for i in range(M):
#    for j in range(N):
#        x = "{0}{1}".format(i, j)
#        input_[i][j] = x

#print input_

def calc_max_r(input_):
    nc = len(input_[0])
    nr = len(input_)
    for c in range((nc + 1) / 2):
        #print c, nc - 1 - c
        for r in range(c):
            print "##",r,c
            #input_[r][c] = 'XXXX'
        for r in range(c, (nr + 1) / 2):
            #print "----",
            #print r, nr -1 -r
            #print input_[r][c], input_[nr -1 -r][c]
            input_[r][c] = "%2d%2d" % (r, c)
            input_[nr -1 -r][c] = "%2d%2d" % (nr -1 -r, c)
            #print input_[r][nc - 1 - c], input_[nr -1 -r][nc - 1 - c]
            input_[r][nc - 1 - c] = "%2d%2d" % (r, nc - 1 - c)
            input_[nr -1 -r][nc - 1 - c] = "%2d%2d" % (nr -1 -r, nc - 1 - c)
            #if r == 1:
            #return
        #print

def calc_max_rax(input_):
    nr = len(input_)
    nc = len(input_[0])
    i = 0
    j = 0
    while i < (nr + 1) / 2 and j < (nc + 1) / 2:
        # print "XXXX"
        # calc
        ml = (nc - i * 2) * 2
        ml += (nr - i * 2 - 2) * 2
        #

        for k in range(j, nc - i):
            #input_[i][k] = "%2d%2d" % (i, k)
            #input_[nr-1-i][k] = "%2d%2d" % (nr-1-i, k)

            input_[i][k] = ml
            input_[nr-1-i][k] = ml
        for sr in range(i+1, nr-1-i):
            #input_[sr][j] = "XXXX"
            #input_[sr][nc - 1 - j] = "XXXX"

            input_[sr][j] = ml
            input_[sr][nc - 1 - j] = ml

        i += 1
        j += 1


calc_max_rax(input_)
for i in input_:
    for j in i:
        print "%4s" % str(j),
    print

#def get_rotation_max(input_):
