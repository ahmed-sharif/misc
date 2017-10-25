


def partition(arr, left, right):
    #print "left", left,"right", right
    if left >= right:
        return 0

    

    i = left
    j = right

    l_sum = arr[i]
    r_sum = arr[j]

    while True:
        if i == j - 1:
            break

        if l_sum < r_sum:
            i += 1
            l_sum += arr[i]
        elif l_sum > r_sum:
            j -= 1
            r_sum += arr[j]
        else:
            i += 1
            j -= 1

            if i == j:
                if arr[i] == 0:
                    i -= 1
                else:
                    l_sum = 1
                    r_sum = 0
                break

            #if arr[i] == 0 and arr[j] == 0:
            #    i -= 1


            l_sum += arr[i]
            r_sum += arr[j]

    if l_sum == r_sum:
        l_count = partition(arr, left, i)
        r_count = partition(arr, j, right)
        #print "ret", max(l_count, r_count) + 1
        return max(l_count, r_count) + 1
    else:
        return 0

"""
arr = [4, 1, 0, 1, 1, 0, 1]
arr = [2, 2, 2, 2]
arr = [3, 3, 3]
"""

test_cases = int(raw_input().strip())

for x in xrange(test_cases):

    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    # print x, arr
    #if x == 9:
    if sum(arr) == 0:
        print n - 1
    else:
        print partition(arr, 0, len(arr) - 1)
