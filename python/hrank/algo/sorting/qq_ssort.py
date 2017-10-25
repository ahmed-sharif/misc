import random

items = [random.randint(1,20) for _ in xrange(15)]
print items




def driver(items):
    quicksort(items, 0, len(items) - 1)
    return items

def quicksort(items, left, right):
    if left >= right:
        return
    
    pivot = partition(items, left, right)
    quicksort(items, left, pivot - 1)
    quicksort(items, pivot, right)


def partition(items, left, right):
    pivot = left + (right - left)/2
    pitem = items[pivot]
    while left <= right:
        while items[left] < pitem:
            left += 1

        while items[right] > pitem:
            right -= 1

        if left <= right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1

    return left

res = driver(items)
print res

assert res == sorted(items)

