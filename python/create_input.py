from random import randint

M = 20
N = 35
R = 20
print M, N, R

for i in range(M):
    for j in range(N):
        print "{0}{1}".format(i+1, j+1),
        # print(randint(1,9)),
    print

