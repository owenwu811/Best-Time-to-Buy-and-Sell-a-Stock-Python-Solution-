

#2229
#easy

#Given an integer array nums, return true if nums is consecutive, otherwise return false.

#An array is consecutive if it contains every number in the range [x, x + n - 1] (inclusive), where x is the minimum number in the array and n is the length of the array.

 

#Example 1:

#Input: nums = [1,3,4,2]
#Output: true
#Explanation:
#The minimum value is 1 and the length of nums is 4.
#All of the values in the range [x, x + n - 1] = [1, 1 + 4 - 1] = [1, 4] = (1, 2, 3, 4) occur in nums.
#Therefore, nums is consecutive.
#Example 2:

#Input: nums = [1,3]
#Output: false
#Explanation:
#The minimum value is 1 and the length of nums is 2.
#The value 2 in the range [x, x + n - 1] = [1, 1 + 2 - 1], = [1, 2] = (1, 2) does not occur in nums.
#Therefore, nums is not consecutive.


#my own solution using python3:

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                return False
        return True
