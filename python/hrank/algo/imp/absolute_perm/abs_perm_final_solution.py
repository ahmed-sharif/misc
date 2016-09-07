
"""
https://www.hackerrank.com/challenges/absolute-permutation
for n = 16, k = 4
diff             [4, 4, 4, 4, 4, 4, 4, 4,  4,  4,  4,  4, 4,   4,  4,  4]
elements         [5, 6, 7, 8, 1, 2, 3, 4, 13, 14, 15, 16, 9,  10, 11, 12]
index (1 based)  [1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16] 


for odd n, the only possible k is 0

for k = 0 the only possible result is:

[1, 2, 3, ......, N]

for other cases
    only possible if n % (2 * k) == 0

    divide the array in n / (2 * k) parts
    divide each part in two halfs
    first fill the right half 
    then  fill the left half

"""
def generate_absolute_permutation(n, k):
    
    # for k = 0
    # res = [1,2,3,....N]
    if k == 0:
        return [str(x) for x in range(1, n + 1)]

    # if n is odd
    # then the only possible k is 0  which is already checked above
    if n % 2 == 1:
        return -1

    rem = n % (2 * k)
    if rem != 0:
        return -1

    result = [0 for _ in range(n)]
        
    outer = n / (2 * k)
    
    number = 1
    for i in range(outer):
        # run this twice in backward direction
        for j in range(1, -1, -1):
            for l in range(k):
                ndx =  i * (2 * k) + k * j + l
                # print i * (2 * k) + k * j + l,
                result[ndx] = str(number)
                number += 1

    return result


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split()
    n,k = [int(n),int(k)]

    r = generate_absolute_permutation(n, k)
    if type(r) is list:
        # print_diff(r)
        print " ".join(r)
    else:
        print -1