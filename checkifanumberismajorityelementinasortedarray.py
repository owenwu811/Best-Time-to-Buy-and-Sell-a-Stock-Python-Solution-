

#1150
#easy

#Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

#A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

 

#Example 1:

#Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
#Output: true
#Explanation: The value 5 appears 5 times and the length of the array is 9.
#Thus, 5 is a majority element because 5 > 9/2 is true.
#Example 2:

#Input: nums = [10,100,101,101], target = 101
#Output: false
#Explanation: The value 101 appears 2 times and the length of the array is 4.
#Thus, 101 is not a majority element because 2 > 4/2 is false.


#my own solution using python3:

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums) / 2
