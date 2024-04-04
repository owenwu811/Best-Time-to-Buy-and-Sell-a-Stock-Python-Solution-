#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

 

#Example 1:

#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#Example 2:

#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9


#my Solution (python3) - 11/7/23:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, maxres = 0, 0
        nums.sort()
        for i in range(len(nums)): #0123456789
            if i > 0 and nums[i] == nums[i - 1]: #
                maxres = max(maxres, res)
                continue
            if i > 0 and nums[i] > nums[i - 1] + 1: #we found a breakpoint, so continue
                maxres = max(maxres, res)
                res = 0
            res += 1
        return max(maxres, res)

#4/3/24 refresher (missed):

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, maxres = 0, 0
        nums.sort()
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]: #[0, 0] only counts as 1 for output
                continue #do not increment res
            if i > 0 and nums[i] - nums[i - 1] > 1:
                maxres = max(res, maxres)
                res = 0
            res += 1
        return max(maxres, res)
 #note that [0, 0, 1, 2, 3, 4, 5, 6, 7, 8] - output is 9 because [0, 0] only counts as 1, so consecutive means increasing
 #why it cannot be return maxres: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] - control flow goes from 1st if to next if without hitting bodies to res += 1, which never updates maxres! so maxres stays 0!
 #why it cannot be return res: nums = [100, 4, 200, 1, 3, 2] - [1, 2, 3, 4, 100, 200] - res gets reset to 0 when i = 4 iteration (nums[i] == 100), so we want result to be 4, not smaller.
 #if res += 1 were placed inside of i > 0 and nums[i] == nums[i - 1] instead of after the 2nd if statement, then 1st iteration of [1, 2, 3, 4, 100, 200], both if statements are False, so the 1st number wouldn't be counted as a result, and result would not be incremented

#practice again :

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, maxres = 0, 0
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: #[0, 0] = 1
                continue #only case where we don't increment res
            if i > 0 and nums[i] - nums[i - 1] > 1:
                maxres = max(res, maxres) #hold historical
                res = 0
            res += 1 #always executes in 1st turn because i = 0 not i > 0 and count the current 1st element always
        return max(res, maxres)
