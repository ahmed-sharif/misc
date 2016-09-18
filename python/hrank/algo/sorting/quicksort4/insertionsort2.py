# https://www.hackerrank.com/challenges/insertionsort2
def print_arr(items):
    for i in items:
        print i,
    print

def insertion_sort(items):
    total = len(items)
    for i in xrange(1, total):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
        print_arr( items)

n = int(raw_input().strip())
items = map(int, raw_input().strip().split())

# insertion_sort([1, 4, 3, 5, 6, 2])
insertion_sort(items)
