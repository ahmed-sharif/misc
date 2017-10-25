# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
divisors = {1: 1, 2: 2, 3: 2, 4: 3, 5:2, 6:4}
antiprimes = {1: True, 2: True, 3: False, 4: True, 5: False, 6: True}

def is_antiprime(number):
    if number in antiprimes:
        # print "cache hit", number
        return antiprimes[number]
    div = find_divisor(number)
    
    for n in range(number -1, 0, -1):
        d = find_divisor(n)
        if d > div:
            antiprimes[number] = False
            return False
    antiprimes[number] = True    
    return True
            

def find_divisor(number):
    if number in divisors:
        # print "cache hit div", number
        return divisors[number]
    total = 2
    limit = int(sqrt(number))
    for x in range(2, limit + 1):
        if(number % x) == 0:
            total += 2
    if sqrt(number) == int(sqrt(number)):
        total -= 1
    divisors[number] = total    
    return total

q = int(raw_input().strip())
for i in range(q):
    inp = int(raw_input().strip())
    # inp = inp + 1
    while True:
        if is_antiprime(inp):
            print inp
            break
        inp += 1
    