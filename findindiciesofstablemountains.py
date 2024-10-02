
#3285
#easy


#There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] represents the height of mountain i, and an integer threshold.

#A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. Note that mountain 0 is not stable.

#Return an array containing the indices of all stable mountains in any order.



#my own solution using python3:

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for i in range(1, len(height)): 
            if height[i - 1] > threshold:
                res.append(i)
        return res
