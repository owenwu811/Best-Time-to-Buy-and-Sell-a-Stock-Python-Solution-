
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#nums = [0,1,0,3,12]
#output: [1,3,12,0,0]


#python3 solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[0, 1, 0, 3, 12]
        #[1, 0, 0, 3, 12]
        #[1, 0, 3, 0, 12]
        #[1, 3, 0, 0, 12]
        #[1, 3, 0, 12, 0]
        #[1, 3, 12, 0, 0]
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0: #the reason we don't do any swapping if left points to a non zero is because left represents the point at which all zeros should be in front of left, so any non zero elements are already in their final place 
                slow += 1
        

#4/8/24:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1

#4/9/24:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[0, 1, 0, 3, 12]
        #[1, 0, 0, 3, 12]
        #[1, 0, 3, 0, 12]
        #[1, 3, 0, 0, 12]
        #[1, 3, 0, 12, 0]
        #[1, 3, 12, 0, 0]
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1


#practice again:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[0, 1, 0, 3, 12]
        #[1, 0, 0, 3, 12]
        #[1, 0, 3, 0, 12]
        #[1, 3, 0, 0, 12]
        #[1, 3, 0, 12, 0]
        #[1, 3, 12, 0, 0]
        l = 0
        for r in range(1, len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1

#4/12/24:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[0, 1, 0, 3, 12]
        #[1, 0, 0, 3, 12]
        #[1, 0, 3, 0, 12]
        #[1, 3, 0, 0, 12]
        #[1, 3, 0, 12, 0]
        #[1, 3, 12, 0, 0]
        left = 0
        for r in range(len(nums)):
            if nums[left] == 0 and nums[r] != 0:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
        

#4/30/24 (missed):

class Solution(object):
    def moveZeroes(self, nums):
        s = 0
        for f in range(len(nums)):
            if nums[s] == 0 and nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
            elif nums[s] != 0: #for loop auto increments left, so if above if is False, then we still need to increment slow - [1, 0, 1] - s and f are both on index 0, so if is False, but s is not equal to 0 since it's equal to 1, so do increment slow, and then for loop call will also increment f so that [1, 0, 1] s and f are now on index 1 after the for loop call
                s += 1


#5/10/24 practice again:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        for r in range(len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1
        
