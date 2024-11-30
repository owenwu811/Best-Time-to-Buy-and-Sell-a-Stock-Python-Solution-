
#3162
#easy

#You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

#A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

#Return the total number of good pairs.

 

#Example 1:

#Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

#Output: 5

#Explanation:

#The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).


#my own solution using python3:

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums1)): 
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    res += 1
        return res
