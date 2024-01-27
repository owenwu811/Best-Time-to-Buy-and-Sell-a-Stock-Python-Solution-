
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


#python3 solution:

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        result = 0
        l, r = 0, len(height) - 1 #two pointer problem
        leftside, rightside = height[l], height[r] 
        while l < r:
            if leftside < rightside:
                l += 1
                leftside = max(leftside, height[l])
                result += (leftside - height[l])
            else: 
                r -= 1
                rightside = max(rightside, height[r])
                result += (rightside - height[r])
        return result



#python3 solution:

#uae two pointer to outermost values of array and set maxleft and maxright initially to the values of those two pointer, subtracting the minimum of maximum historical coming inwards between left and right sides from the current inner value and add this value to result
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        maxleft, maxright = height[l], height[r]
        while l < r: #will end on l and r being on the highest elevation where you know you can't trap any water at highest elevation since we are constrained by minimum, and we visited all other elements in array since we came from outward inwards
            if maxright < maxleft:
                r -= 1
                maxright = max(maxright, height[r])
                #res only increases from this line if above line's maxright historical won out meaning current inner is smaller than historical from tha side - 1 may be historical and 0 may be current, so we can trap 1
                res += (maxright - height[r])
            else:
                l += 1
                maxleft = max(maxleft, height[l])
                res += (maxleft - height[l])
        return res
        
#12/30/23 refresher - my solution in python3:

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        maxleft, maxright = height[l], height[r]
        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                res += (maxleft - height[l])
            elif maxleft == maxright:
                r -= 1
                maxright = max(maxright, height[r])
                res += (maxright - height[r])
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += (maxright - height[r])
        return res
        
#1/3/24 refresher - my solution in python3:

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]
        res = 0
        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                res += (maxleft - height[l])
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += (maxright - height[r])
        return res



#1/7/24 refresher solution:

class Solution:
    def trap(self, height: List[int]) -> int:
        #don't forget to acount for this edge case!!!! - if the array has no elements, then we can't trap any water, so return 0 as the maximum units of water we can trap!
        if not height:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        maxleft, maxright = height[l], height[r]
        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                res += (maxleft - height[l])
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += (maxright - height[r])
        return res


#1/15 refresher - my own solution in python3:

class Solution:
    def trap(self, height: List[int]) -> int:
        #we are given and array of integers, that, at the very least are equal to 0 if not greater than 0
        #we want to find how much water we can trap at each level that is restricted by the smaller of the two heights minus the current height
        #our array is empty [], so we can't trap any water, so return 0 units of water trapped
        if not height:
            return 0
        res = 0
        #indexes starting at the beginning and end of the array
        l, r = 0, len(height) - 1
        #l and r indexes will meet at the highest level where we can't trap any water at the highest level because we are bounded to the lower of the two heights, so l <= r is not necessary 
        maxleft, maxright = height[l], height[r]
        while l < r:
            #we want to reduce the number of restrictions, so we move the pointer with the smaller height
            if maxleft < maxright:
                l += 1
                #if maxleft wins out, result will be greater than it was before. If height[l] wins out, we can't trap anymore water
                maxleft = max(maxleft, height[l])
                if maxleft > height[l]:
                    res += (maxleft - height[l])
            else:
                r -= 1
                maxright = max(maxright, height[r])
                if maxright > height[r]:
                    res += (maxright - height[r])
        return res


#1/27/24 refresher:

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        leftside = height[l]
        rightside = height[r]
        while l < r:
            if leftside < rightside:
                l += 1
                leftside = max(leftside, height[l])
                res += (leftside - height[l])
            else:
                r -= 1
                rightside = max(rightside, height[r])
                res += (rightside - height[r])
        return res
