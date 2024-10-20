
#Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

#Return the array ans.

 

#Example 1:

#Input: nums = [1,2,3,2,2,1,3], k = 3
#Output: [3,2,2,2,3]
#Explanation: The number of distinct elements in each subarray goes as follows:
#- nums[0:2] = [1,2,3] so ans[0] = 3
#- nums[1:3] = [2,3,2] so ans[1] = 2
#- nums[2:4] = [3,2,2] so ans[2] = 2
#- nums[3:5] = [2,2,1] so ans[3] = 2
#- nums[4:6] = [2,1,3] so ans[4] = 3
#Example 2:

#Input: nums = [1,1,1,1,2,3,4], k = 4
#Output: [1,2,3,4]
#Explanation: The number of distinct elements in each subarray goes as follows:
#- nums[0:3] = [1,1,1,1] so ans[0] = 1
#- nums[1:4] = [1,1,1,2] so ans[1] = 2
#- nums[2:5] = [1,1,2,3] so ans[2] = 3
#- nums[3:6] = [1,2,3,4] so ans[3] = 4


#my own solution using python3 after a small hint from chatgpt regarding len(set(firstwindow)) vs. len(firstwindow):

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res = []
        firstwindow = Counter(nums[:k])
        print(firstwindow)
        res.append(len(set(firstwindow.keys())))
        for i in range(1, len(nums) - k + 1):
            end = nums[i + k - 1]
            #print(end)
            beg = nums[i - 1]
            #print(beg)
            firstwindow[end] += 1
            firstwindow[beg] -= 1
            if firstwindow[beg] == 0:
                del firstwindow[beg]
            cur = 0
            res.append(len(firstwindow))
        return res
        #[1, 2, 3] > [2, 3, 2]
        #2 increases by 1, 3 stays the same, 1 decreases by one
            
