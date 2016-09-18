# https://www.hackerrank.com/challenges/tutorial-intro


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) / 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"""
n = int(raw_input().strip())
raw_input().strip()

items = map(int, raw_input().strip().split())
print binary_search(items, n)

print binary_search([1, 4, 5, 7, 9, 12], 4)
print binary_search([1, 4, 5, 7, 9, 12], 9)
print binary_search([1, 4, 5, 7, 9, 12], 12)
print binary_search([1, 4, 5, 7, 9, 12], 6)
print binary_search([1, 4, 5, 7, 9, 12], 8)
print binary_search([1, 4, 5, 7, 9, 12], 43)
"""
print binary_search([1, 4], 4)
print binary_search([1, 4], 1)
print binary_search([1, 4], 15)
print binary_search([11, 14], 5)
