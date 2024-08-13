#medium
#73.8%acceptancerate


#It is a sweltering summer day, and a boy wants to buy some ice cream bars.

#At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

#Note: The boy can buy the ice cream bars in any order.

#Return the maximum number of ice cream bars the boy can buy with coins coins.

#You must solve the problem by counting sort.

#Input: costs = [1,3,2,4,1], coins = 7
#Output: 4
#Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

#after hint, I was able to solve by myself - this is greedy, not DP

#my own solution using python3:


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        costs.sort()
        for cost in costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                coins = coins
        return res

