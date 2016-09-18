# https://www.hackerrank.com/challenges/quicksort4

total_swp = 0

def print_arr(items):
    for i in items:
        print i,
    print


def insertion_sort(items):
    total_ins_swp = 0
    total = len(items)
    for i in xrange(1, total):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
            total_ins_swp += 1
        items[j + 1] = key
        # print_arr( items)
    return total_ins_swp

def quick_sort(items, l, r):
    if l >= r:
        return
    # print_arr(items[l:r+1])
    p = partition(items, l, r)
    # print "pivot", p
    quick_sort(items, l, p - 1)
    quick_sort(items, p + 1, r)



def partition(items, l, r):
    global total_swp
    pivot = items[l]
    j = l
    
    for i in xrange(l + 1, r + 1):
        if items[i] <= pivot:
            j += 1
            items[j] , items[i] = items[i], items[j]
        
            total_swp += 1
    items[j], items[l] = items[l], items[j]
    total_swp += 1
    return j
            
import copy        

# n = int(raw_input().strip())
# items = map(int, raw_input().strip().split())
# items = [4, 5, 3, 7, 2]
# items = [5, 8, 1, 3, 7, 9, 2]
items = [1, 3, 9, 8, 2, 7, 5]
items2 = copy.copy(items)
print items
quick_sort(items, 0 , len(items) - 1)
print_arr(items)
print total_swp


print insertion_sort(items2)
