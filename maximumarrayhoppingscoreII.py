
#3221
#medium


#Given an array nums, you have to get the maximum score starting from index 0 and hopping until you reach the last element of the array.

#In each hop, you can jump from index i to an index j > i, and you get a score of (j - i) * nums[j].

#Return the maximum score you can get.

 

#Example 1:

#Input: nums = [1,5,8]

#Output: 16

#Explanation:

#There are two possible ways to reach the last element:

#0 -> 1 -> 2 with a score of (1 - 0) * 5 + (2 - 1) * 8 = 13.
#0 -> 2 with a score of (2 - 0) * 8 = 16.


#correct python3 solution: (could not solve)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res, maxh = 0, 0
        for i in range(len(nums) -1, 0, -1):
            maxh = max(maxh, nums[i])
            res += maxh
        return res
