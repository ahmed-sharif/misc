


"""
Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 12
Two subarrays are [-2, -3] and [4, -1, -2, 1, 5]

Input: [2, -1, -2, 1, -4, 2, 8]
Output: 16
Two subarrays are [-1, -2, 1, -4] and [2, 8] 

"""

Input= [-2, -3, 4, -1, -2, 1, 5, -3]


total = sum(Input)


left = 0
right = total
mx = 0
print Input
print total
for i in xrange(len(Input) - 1):
    left += Input[i]

    right -= Input[i]
    print i, left, right


    if abs(left - right) > mx:
        mx = abs(left - right)

print mx
    
