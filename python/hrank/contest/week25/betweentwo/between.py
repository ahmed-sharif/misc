
from fractions import gcd

n,m = map(int,raw_input().strip().split())
a = map(int,raw_input().strip().split())
b = map(int,raw_input().strip().split())

def lcm(a, b):
    gc = gcd(a, b)
    return (a * b) / gc


def lcm_list(l):
    r = reduce(lcm, l)
    return r



def gcd_list(l):
    return reduce(gcd, l)


a_gcd = lcm_list(a)
b_gcd = gcd_list(b)
    

if b_gcd % a_gcd == 0:
    if b_gcd == a_gcd:
        total = 1
    else:
        total = 2
        start = 2 * a_gcd
        while start < b_gcd:
            #print "start",start
            if b_gcd % start == 0:
                total += 1
            start += a_gcd

    print total
else:
    print 0