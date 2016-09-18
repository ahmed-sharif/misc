# https://www.hackerrank.com/challenges/quicksort2
def print_arr(items):
    for i in items:
        print i,
    print



def quick_sort(items, l, r):
    if l >= r:
        return
    print_arr(items[l:r+1])
    p = partition(items, l, r)
    print "pivot", p
    quick_sort(items, l, p - 1)
    quick_sort(items, p + 1, r)



def partition(items, l, r):
    pivot = items[l]
    j = l

    for i in xrange(l + 1, len(items)):
        if items[i] <= pivot:
            j += 1
            items[j] , items[i] = items[i], items[j]
    items[j], items[l] = items[l], items[j]
    return j
            
        

# n = int(raw_input().strip())
# items = map(int, raw_input().strip().split())
# items = [4, 5, 3, 7, 2]
items = [5, 8, 1, 3, 7, 9, 2]
print items
quick_sort(items, 0 , len(items) - 1)
print_arr(items)
