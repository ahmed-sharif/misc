# https://www.hackerrank.com/challenges/countingsort1
def print_arr(items):
    for i in items:
        print i,
    print


n = int(raw_input().strip())
items = map(int, raw_input().strip().split())

counts = [0 for _ in xrange(100)]

for i in items:
    counts[i] += 1

print_arr(counts)
