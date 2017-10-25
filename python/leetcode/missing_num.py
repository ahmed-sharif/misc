"""
class Solution(object):
    def missingNumber(self, nums):
        i = 0
        while i < len(nums):
            print nums
            number_at_i = nums[i]
            expected_number = i
            
            if number_at_i != expected_number and number_at_i < len(nums):
                nums[expected_number], nums[i] = nums[i], nums[expected_number]
            else:
                i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
        
        return len(nums)
"""                
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        i = 0
        res = []
        while i < len(nums):
            if nums[i] != i + 1:
                res.append(i + 1)
            i += 1
        return res
                        
            
s = Solution()
print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])




