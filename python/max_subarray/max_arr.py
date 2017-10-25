





def max_sub_array(arr):
    running_total = 0
    max_so_far = 0
    end_index = 0
    start_index = 0
    for ind, i in enumerate(arr):
        running_total += i

        if running_total <= 0:
            running_total = 0
            start_index = ind+1
        if running_total >= max_so_far:
            max_so_far = running_total
            end_index = ind
    return max_so_far, start_index, end_index

print max_sub_array([904, 40, 523, 12, -335, -385, -124, 481, -31])


nums = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]      
print max_sub_array(nums)
nums = [-11, -3, -5, -4, -6, -10, -2, -7, -13, -3]
print max_sub_array(nums)