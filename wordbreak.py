
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

#Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

#Example 1:

#Input: s = "leetcode", wordDict = ["leet","code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".



#python3 solution:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we want to make sure every character in s meaning the entire string can be space segmented. if even one last character in s cannot be space segmented, we return false, which we assume by filling the array initially with false except for the first character in s 
        #remember - empty string is considered breakable, which is why we set the 1st element to True and all others to False!
        dp = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict: #This condition checks whether the current substring is in the word dictionary. If it is, it means we can break the string up to this point.
                    #set the farthest cell between i and j + 1 that's not yet true to true - this is why we set i to true initially - we want it to trigger the farther cell to turn true so we can mark the progress we have made
                    dp[j + 1] = dp[i] or dp[j + 1]
        #if the entire string - every last character - can be space segmented, we return True as we have flipped that last character to True. Otherwise, we don't modify it, and it stays False
        return dp[-1] 


#1/17/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = dp[i] or dp[j + 1]
        return dp[-1]


#1/18/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]


#1/18/24 refresher #2:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]


#1/25/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]



#1/26/24 refresher:

res = [True] + [False] * len(s)
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i: j + 1] in wordDict:
            res[j + 1] = res[i] or res[j + 1]
return res[-1]


#2/1/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]



#2/3/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we want to return True only if the ENTIRE string s can be divided exactly without overlap amoung words in the dictionary
        res = [True] + [False] * len(s)
        for windowstartchar in range(len(s)):
            for windowendchar in range(windowstartchar, len(s)):
                if s[windowstartchar: windowendchar + 1] in wordDict:
                    res[windowendchar + 1] = res[windowstartchar] or res[windowendchar + 1]
        return res[-1]
                

#2/6/24:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]


#2/10/24:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we want to return a boolean to see if we can space segement the ENTIRE string s based on what is in our list of strings
        res = [True] + ([False] * len(s))
        for l in range(len(s)):
            for r in range(l, len(s)):
                if s[l: r + 1] in wordDict:
                    res[r + 1] = res[l] or res[r + 1] #res[r + 1] not s[r + 1] because we want to modify the boolean at that position in the res list that we will eventually return the last boolean once we finish making all windows in s
        return res[-1]

#2/14/24:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]

#3/1/24:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]

#3/8/24:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]


#The "word break" problem is a classic dynamic programming problem frequently encountered in coding interviews and coding challenges like those found on LeetCode. The problem statement typically goes like this:

#Given a string s and a dictionary of words, you are asked to determine if s can be segmented into a space-separated sequence of one or more dictionary words.

#For example, given the string "leetcode" and the dictionary ["leet", "code"], return true because "leetcode" can be segmented as "leet code".

#The key concepts and techniques involved in solving the word break problem include:

#Dynamic Programming (DP):
#This problem can be efficiently solved using dynamic programming. The idea is to build up a dynamic programming table where each cell dp[i] represents whether the substring ending at index i (i.e., s[0:i+1]) can be segmented into valid words from the dictionary. The value of dp[i] is determined by checking whether any prefix of s[0:i+1] is a valid word and if the rest of the substring (excluding that prefix) can also be segmented.

#Memoization:
#While implementing dynamic programming, memoization can be used to store the results of subproblems that have already been solved, which helps avoid redundant calculations and improves efficiency.

#Dictionary Lookup:
#The problem involves checking whether substrings of the given string exist in a dictionary of words. An efficient data structure like a hash set or trie can be used to store the dictionary for faster lookup operations.

#String Manipulation:
#Iterating over the string and breaking it into substrings to check their presence in the dictionary is a fundamental aspect of solving this problem.

#Recursion (optional):
#While not always the most efficient approach, you may encounter recursive solutions to the word break problem as well. Recursion can be used to explore all possible segmentations of the string, but often leads to inefficient time complexity if not optimized properly.
