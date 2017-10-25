




def is_possible(a, b):
    return sum(a) == sum(b)


def find_diff(a, b):
    total_equal = 0
    for i in range(len(a)):

        if a[i] > b[i]:
            total_equal += a[i] - b[i]


    return total_equal

n = int(raw_input().strip())
a = map(int, raw_input().strip().split()) 
b = map(int, raw_input().strip().split())

if is_possible(a, b):
    a.sort()
    b.sort()
    print find_diff(a, b)
else:
    print -1

"""               
a = [1, 4, 12, 14, 16]
b = [1, 5, 10, 15, 16]

print find_diff(a, b)
print find_diff(b, a)
n = 5
a = [1,   2, 3, 4, 5]
b = [-9, -1, 5, 8, 12]
print find_diff(a, b)
print find_diff(b, a)


a= [1, 2, 3]
b = [-1, 3, 4]

print find_diff(a, b)
print find_diff(b, a)


a = [1, 4, 12, 14, 16]
b = [16, 15, 10, 1, 5]

print find_diff(a, b)
print find_diff(b, a)
"""
