
#1822


#There is a function signFunc(x) that returns:

#1 if x is positive.
#-1 if x is negative.
#0 if x is equal to 0.
#You are given an integer array nums. Let product be the product of all values in the array nums.

#Return signFunc(product).

#my own solution using python3:

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        f = 1
        for n in nums:
            f *= n
        if f > 0:
            return 1
        elif f < 0:
            return -1
        else:
            return 0
        
