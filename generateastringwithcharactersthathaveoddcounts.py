
#1374
#easy


#Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

#The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

#Example 1:

#Input: n = 4
#Output: "pppz"
#Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".



#my own solution using python3:

class Solution:
    def generateTheString(self, n: int) -> str:
        letters = "ab"
        res = ""
        if n % 2 == 0:
            res += ("a" * (n - 1))
            print(res)
            res += "b"
            return res


        if n % 2 != 0:
            res += ("a" * (n))
            return res
