




primes = [1 for _ in range(20+1)]

import math

for i in range(2, int(math.sqrt(21)+1)):
    if primes[i] == 0:
        continue
    for j in range(i+i,21,i):
        primes[j] = 0
        
print primes

for i in range(2, len( primes)):
    if primes[i] == 1:
        print i,
print
