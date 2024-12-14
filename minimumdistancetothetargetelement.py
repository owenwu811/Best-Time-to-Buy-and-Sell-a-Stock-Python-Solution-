
#1848
#easy

#Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

#Return abs(i - start).

#It is guaranteed that target exists in nums.

 

#Example 1:

#Input: nums = [1,2,3,4,5], target = 5, start = 3
#Output: 1
#Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
#Example 2:

#Input: nums = [1], target = 1, start = 0
#Output: 0
#Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.


#my own solution using python3:

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                print(abs(i - start))
                res = min(res, abs(i - start))
        return res
