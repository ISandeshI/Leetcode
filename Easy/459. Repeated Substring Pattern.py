# 459. Repeated Substring Pattern
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str):
        len1 = len(s)
        for i in range (1, (len1//2) + 1):
            if len1 % i == 0:
                if s[:i] * (len1 / i) == s:
                    return True
                
        else:
            return False

"""
I totaly check in chatgpt for logic to implement it, because tried multiple ways yet my tricks failed.
This solution runs in 7ms and beats 54% + solutions out there.
Yet there is an one line solution:

return s in (s + s)[1:-1]

Why this works?

If s is built by repeating a substring, it will appear inside (s + s) excluding first & last characters
Otherwise, it won't

Example:
s = "abab"
s+s = "abababab"
(s+s)[1:-1] = "bababa"
"abab" in "bababa" → True
"""