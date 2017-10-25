def max_array(arr):
    
    res = [arr[0]]
    for i in range(1, len(arr)):
      res.append(res[i-1] + arr[i])
    print res

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
