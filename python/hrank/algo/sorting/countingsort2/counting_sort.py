# https://www.hackerrank.com/challenges/countingsort2

n = int(raw_input().strip())
items = map(int, raw_input().strip().split())

counts = [0 for _ in xrange(100)]

for i in items:
    counts[i] += 1

for index, item in enumerate(counts):
    for _ in xrange(item):
        print index,
    
print
# print_arr(counts)
