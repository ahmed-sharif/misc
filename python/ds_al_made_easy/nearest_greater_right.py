import random

n = 10
items = [random.randrange(n+1) for _ in xrange(n)]
print items


def find_nearest_brute_force(items):
    result = [-1 for _ in xrange(len(items))]
    for i in xrange(0, len(items) - 1):
        for j in xrange(i + 1, len(items)):
            if items[j] > items[i]:
                result[i] = items[j]
                break
    return result            



def find_nearest(items):
    result = [-1 for _ in xrange(len(items))]
    stack = []
    i = 1
    while i < n:
        if items[i] > items[i-1]:
            result[i - 1] = items[i]

            while stack and items[stack[-1]] < items[i]:
                result[stack[-1]] = items[i]
                stack.pop()
            
        else:
            stack.append(i - 1)
        i += 1

    return result

r1 = find_nearest(items)
r2 = find_nearest_brute_force(items)
print r1
print r2
assert r1 == r2







