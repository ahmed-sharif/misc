# https://www.hackerrank.com/challenges/runningtime


def insertion_sort(items):
    total = len(items)
    shift_count = 0
    for i in xrange(1, total):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
            shift_count += 1
        items[j + 1] = key
    print shift_count

n = int(raw_input().strip())
items = map(int, raw_input().strip().split())

# insertion_sort([2, 1, 3, 1, 2])
insertion_sort(items)
