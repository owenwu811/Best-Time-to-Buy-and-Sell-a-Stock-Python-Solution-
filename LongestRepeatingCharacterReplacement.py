You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


My Solution:
  
  class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength = 0
        windowstart = 0
        char_freq = {}
        max_char_freq = 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] += 1
            max_char_freq = max(max_char_freq, char_freq[right_char])
            currlength = window_end - windowstart + 1
            if currlength - max_char_freq > k: #represents the number of characters in current substring that aren't most frequently occuring 
            #and the reason we want the not most frequently occuring is because it always makes sense to flip the character with less number of flips to make everything equal
                #if the number is bigger than k, we have to change more than k characters to get a valid substring consisting of only a single character, so shrink the window by moving windowstart to the right
                left_char = s[windowstart]
                char_freq[left_char] -= 1 #when we shrink the window, we have to reflect that change in our dictionary
                windowstart += 1
            maxlength = max(maxlength, window_end - windowstart + 1)
        return maxlength
#shrinking the window is only used to fufill the k condition

            
#max_char_freq is the frequency of most frequently occuring character in current window while max_len is the length of the longest substring with same character seen so far 
            
