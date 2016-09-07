import itertools

def print_perm(perm):
    for p in itertools.permutations(perm):
        s = [abs(p[i-1] - i) for i in range(1,len(p)+1)]
        # print s
        item = s[0]
        for xxx in range(1, len(s)):
            if s[xxx] != item:
                break
        else:
            print s
            print p
            print "---------"



def print_diff(p):
    s = [abs(p[i-1] - i) for i in range(1,len(p)+1)]
    print len(p)
    print s
    print p
    print "---------"

"""
n = 4
l = [x for x in range(1,n+1)]
print_perm(l)


n = 5
l = [x for x in range(1,n+1)]
print_perm(l)

n = 6
l = [x for x in range(1,n+1)]
print_perm(l)

#n = 7
#l = [x for x in range(1,n+1)]
#print_perm(l)

n = 8
l = [x for x in range(1,n+1)]
print_perm(l)

#n = 9
#l = [x for x in range(1,n+1)]
#print_perm(l)


n = 10
l = [x for x in range(1,n+1)]
print_perm(l)

n = 12
l = [x for x in range(1,n+1)]
print_perm(l)

# 4 4 4 4 4 4 4 4  4  
# [5,6,7,8,1,2,3,4, 13,14,15,16, 9 10,11,12]


l = [5,6,7,8,1,2,3,4, 13,14,15,16, 9, 10,11,12]
print_diff(l)

l = [6,7,8,9,10, 1,2,3,4,5, 16,17,18,19,20, 11,12,13,14,15]
print len(l)
print_diff(l)

l = [3,4,1,2,   7, 8,5,6,  11,12, 9,10,     15,16,13, 14,       19,20,17,18]
print len(l)
print_diff(l)


"""

def generate_absolute_permutation(n, k):
    # if n is odd
    # then the only possible k is 0
    if n % 2 == 1:
        if k == 0:
            return [str(x) for x in range(1, n + 1)]
        else:
            return -1

    rem = n % (2 * k)
    if rem != 0:
        return -1

    result = [0 for _ in range(n)]
        
    outer = n / (2 * k)
    inner = 2 * k
    number = 1
    for i in range(outer):
        for j in range(1, -1, -1):
            for l in range(k):
                ndx =  i * (2 * k) + k * j + l
                # print i * (2 * k) + k * j + l,
                result[ndx] = str(number)
                number += 1

    return result


targets = [
    (20, 5),
    (20, 2),
    (6, 3),
    (6, 5),
    (3,0),
    (3,1),
]

targets = [
    (2, 1),
    (3, 0),
    (3, 2)
]


for (n,k) in targets:
    r = generate_absolute_permutation(n, k)
    if type(r) is list:
        # print_diff(r)
        print " ".join(r)
    elif r == -1:
        print -1
    else:
        print

#r = generate_absolute_permutation(20, 5)
#print_diff(r)

#r = generate_absolute_permutation(20, 5)
#print_diff(r)

