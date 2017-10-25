# Enter your code here. Read input from STDIN. Print output to STDOUT
import pprint

M, N = raw_input().strip().split()

M = int(M)
N = int(N)
# R = int(R)

# M rows
# N cols

input_ = []
cache = []
rotation_max = []
for _ in xrange(M):
    input_.append([None] * N)
    cache.append([None] * N)
    rotation_max.append([99] * N)

def get_rotation_max(input_):
    c = 0
    for i in range(len(input_)/2):
        if i >= len(input_[0])/2:
            return
        l = (len(input_[0]) - i*2 ) * 2
        l += (len(input_)-1 - i - i -1) * 2

        for j in range(i,len(input_[0])-i):
            rotation_max[i][j] = l
            rotation_max[len(input_)-i-1][j] = l
        # return
        for row in range(i+1, len(input_)-i-1):
            # print row, c
            # print row, len(input_[0])-c-1
            rotation_max[row][c] = l
            rotation_max[row][len(input_[0])-c-1] = l
        c +=1
        
        #if i == 1:
        #    return
        if len(input_[0])==2:
            break



def calc_rotation_max(input_):
    for  i in xrange((len(input_)+1)/2):
        print "i=",i,
        print len(input_)-1-i

        for j in xrange((len(input_[0])+1)/2):
            print "j=",j



calc_rotation_max(input_)
for p in rotation_max:
    print p
# pprint.pprint(rotation_max) 