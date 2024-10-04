
#1991

#easy


#Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

#A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

#If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

#Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

#Input: nums = [2,3,-1,8,4]
#Output: 3
#Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
#The sum of the numbers after index 3 is: 4 = 4


#my own solution using python3:

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1
