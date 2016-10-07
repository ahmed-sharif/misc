# https://www.hackerrank.com/challenges/bigger-is-greater

def next_permutation(items):
    # find increasing sequence from end
    k = len(items) -2
    while k >= 0 and items[k] >= items[k+1]:
        k -= 1

    # if the whole sequence is increasing from end
    # then there is no sulution    
    if k == -1:
        return False

    # search in Arr[k+1 : end] to get the smallest item greater than Arr[k]
    last = len(items) - 1
    while last > k:
        if items[last] > items[k]:
            break
        last -= 1

    items[k], items[last] = items[last], items[k]


    last = len(items) - 1
    half = (len(items) - 1 - k) / 2
    for i in range(half):
        items[k +1 + i], items[last - i] = items[last - i], items[k +1 + i]

    return True
"""
next_permutation(['d', 'k', 'h', 'c'])
"""
test_cases = int(raw_input().strip())
for i in range(test_cases):
    items = list(raw_input().strip())

    got_solution = next_permutation(items)
    if got_solution:
        print "".join(items)
    else:
        print "no answer"
