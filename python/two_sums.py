nums = [21, 2, 5, 7, 11, 15, 7]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        start = 0
        end = len(sorted_nums) - 1
        while start < end:
            current_sum = sorted_nums[start] + sorted_nums[end]
            if(current_sum == target):
                start_index = nums.index(sorted_nums[start])
                nums[start_index] = None
                end_index = nums.index(sorted_nums[end])
                nums[start_index] = sorted_nums[start]
                return [start_index, end_index]
            if(current_sum > target):
                end -= 1
            else:
                start += 1
        return []



s = Solution()
print s.twoSum(nums, target)
target = 100
print s.twoSum(nums, target)
target = 14
print s.twoSum(nums, target)
            
