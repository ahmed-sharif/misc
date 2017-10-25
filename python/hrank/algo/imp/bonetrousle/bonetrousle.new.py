


"""

brain storming
---------
n(3)    = n(n+1)/2  = 3*4/2 = 6
n(18)   = 18*19/2 =   171


n(18-3)
n(15)   =  15*16/2 = 120
            16 + 17 + 18  = 51  
n(18) - n(15) = 171 - 120 = 51

min = 6

max = 51
---------

1 2 3 = 6
2 3 4 = 9
3 4 5 = 12

4 5 6 = 15
5 6 7 = 18
6 7 8 = 21
7 8 9 = 24


n = 3

------------
24 - 6 = 18

18 / 3 = 6

1 + 6 = 7

7 8 9 = 24
-----------
25 - 6 = 19
19 / 3 = 6

19 % 3 = 1

1 + 6 = 7
7 8 10 = 25
-------------------

rem = target - min
qu  = rem / n 
re  = rem % n

start = 1 + qu

for i=1 to n-1
  print start
  start ++
print start + re

------------------


"""


def get_sum(n):
    return (n * (n + 1)) / 2


def solution(target, options, n):
    minimum = get_sum(n)

    maximum = get_sum(options) - get_sum(options - n)

    if not (target >= minimum and target <= maximum):
        return [-1]

    results = []    
    rem = target - minimum
    quotent = rem / n 
    re = rem % n

    start = 1 + quotent

    for i in range(n-1):
        results.append(start)
        start += 1
    results.append(start + re)
    return results

"""
n = 3
target = 24
a = [0 for _ in range(n)]
option = 18
current_sum = 0
solution_found = backtrack(a, 0, n, target, option, current_sum)
if solution_found:
    print a
else:
    print -1

# target  option  n

solution (12, 8, 3)
solution (10, 3, 3)
solution (9, 10, 2)
solution (9, 10 ,2)
"""

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    target, option, n = map(int, raw_input().strip().split())
    
    a = solution(target, option, n)
    
    a = map(str, a)
    print " ".join(a)