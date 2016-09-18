# https://www.hackerrank.com/challenges/insertionsort2
def print_arr(items):
    for i in items:
        print i,
    print



def insertion_sort(items):
    total = len(items)
    for i in xrange(1, total):
        item = items[i]
        last_location = i
        for j in xrange(i - 1, -1, -1):
            if items[j] > item:
                items[j + 1] = items[j]
                last_location = j
                # print_arr( items)
        if last_location != i:
            items[last_location] = item
            # print_arr( items)
        print_arr( items)


n = int(raw_input().strip())
items = map(int, raw_input().strip().split())

# insertion_sort([2, 4, 6, 8, 3])
insertion_sort(items)
