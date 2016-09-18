# https://www.hackerrank.com/challenges/quicksort1
def print_arr(items):
    for i in items:
        print i,
    print


def partition(items):
    pivot = items[0]
    left = []
    right = []
    equal = [pivot]
    for ind in xrange(1, len(items)):
        if items[ind] < pivot:
            left.append(items[ind])
        elif items[ind] > pivot:
            right.append(items[ind])
        else:
            equal.append(items[ind])
    return left + equal + right
            
        

n = int(raw_input().strip())
items = map(int, raw_input().strip().split())
# items = [4, 5, 3, 7, 2]
items = partition(items)
print_arr(items)
