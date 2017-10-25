import sys

def gcd(a, b):
    x = a
    y = b

    if x < y:
      temp = x
      x = y
      y = temp

    res = x % y

    while res:
        x = y
        y = res
        res = x % y

    return y    

def mulp_gcd(numbers):
    return reduce(gcd, numbers)

def mul_gcd(numbers):
    if 2 in numbers:
        return 2
    return reduce(gcd, numbers)

def is_prime(num):
    x = 2
    while (x * x) <= num:
        if num % x == 0:
            return False
        x += 1
    return True

def sol(numbers, k):
    if k == 1:
        return 0
    g = mul_gcd(numbers)
    # print g
    # print "----"
    if len(numbers) == 1:
        if is_prime(g):
            if g == k:
                return k
            else:
                return 0
    # if g > k:
    #     return 0

    res = 0

    end = 2
    start = k

    g_is_prime = is_prime(g)

    while start >= end:
        n_gcd = mulp_gcd([g, start])
        if n_gcd != 1:
            return start
        if start > g:
            if g_is_prime:
                start = start - (start % g)
            else:
                start -= 1
        else:
            if g_is_prime:
                return 0
            else:
                start -= 1

    return res


"""

print "gcd(15,10)=", gcd(15,10)
print "gcd(10,10)=", gcd(10,10)
print "gcd(1,7)=", gcd(1,7)
print "gcd(7,1)=", gcd(7,1)
print "gcd(5,7)=", gcd(5,7)
print "gcd(7,5)=", gcd(7,5)

"""




n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
# A = raw_input().strip().split(' ')
A = map(int,raw_input().strip().split(' '))


print sol(set(A), k)
