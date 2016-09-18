# https://www.hackerrank.com/challenges/missing-numbers
n = int(raw_input().strip())
a_list = map(int, raw_input().strip().split())
m = int(raw_input().strip())
b_list = map(int, raw_input().strip().split())


frequency = [0 for _ in xrange(10000 + 1)]

for item in b_list:
    frequency[item] += 1

for item in a_list:
    frequency[item] -= 1

for index, item in enumerate(frequency):
    if item != 0:
        print index,
