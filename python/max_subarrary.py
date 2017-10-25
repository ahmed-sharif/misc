def max_array(arr):
    current_sum = 0
    start_index = 0
    current_start_index = 0
    end_index = 0
    max_sum = 0
    max_non_contiguous_sum = 0
    max_neg_num = arr[0]

    for i in range(len(arr)):

        if arr[i] > 0:
            max_non_contiguous_sum += arr[i]

        if arr[i] > max_neg_num:
            max_neg_num = arr[i]

        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
            start_index = current_start_index

        if current_sum < 0:
            current_start_index = i + 1
            current_sum = 0
    # print "max = ", max_sum
    # print arr[start_index:end_index+1]

    if max_sum == 0:
        # print "max = ", max_neg_num
        return max_neg_num, max_neg_num
    else:
        return max_sum, max_non_contiguous_sum

nums = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]      
print max_array(nums)
nums = [-11, -3, -5, -4, -6, -10, -2, -7, -13, -3]
print max_array(nums)
"""
test_cases = int(raw_input().strip())

for _ in range(test_cases):
    raw_input()
    numbers = raw_input().strip().split()
    numbers = [int(n) for n in numbers]
    cont, non_cont = max_array(numbers)
    print cont, non_cont

"""

