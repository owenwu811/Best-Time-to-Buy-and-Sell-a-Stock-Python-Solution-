
#3110
#easy

#You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

#Return the score of s.

 

#Example 1:

#Input: s = "hello"

#Output: 13

#Explanation:

#The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.


#my own solution using python3:


class Solution:
    def scoreOfString(self, s: str) -> int:
        print(ord("h"))
        res = 0
        for i in range(1, len(s)):
            cur = abs(ord(s[i]) - ord(s[i - 1]))
            print(cur)
            res += cur
        return res

