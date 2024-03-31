#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

#Return the max sliding window.

#nums = [1,3,-1,-3,5,3,6,7], k = 3
#output: [3,3,5,5,6,7]


#python3 solution:


class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            #before adding 5 to our deque, we must check if 5 is greater than the value at top of deque. if it is, since 5 > 4, then don't consider 4 as max value ever again = [1, 1, 1, 1, 1, 4, 5], k = 6
            while q and nums[q[-1]] < nums[r]: 
                q.pop() #since we don't consider 4 as max value ever again since 5 > 4, pop 4 from deque
            q.append(r) #add 5 to the top 
            if l > q[0]: #[8, 7, 6, 9], k = 2. deque = [7, 6]. our window is [6, 9], so since 7 is no longer in bounds, and max value in our window is 7, we add 7 to the output before we pop 7 from our deque
                q.popleft() #the action of popping 7 from our deque
            if (r + 1) >= k: 
                output.append(nums[q[0]]) #since our deque is always in decreasing order [8, 7], we can look at the leftmost value in our deque [8, 7] - 8 - and add 8 (leftmost) to our output
                l += 1
            r += 1
        return output

