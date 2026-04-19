# 1614. Maximum Nesting Depth of the Parentheses
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3

 

# Constraints:

# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxCount = 0
        n = len(s)

        for i in range(n):
            if s[i] == "(":
                count += 1
                maxCount = max(maxCount, count)
            elif s[i] == ")":
                count -= 1
            if i >= (2*n - 1 - maxCount):
                break
            # skipping unwanted pairs (if they exists) who are going to be less than what 
            # we found highest till the time.

        return maxCount
    
"""
Runtime is 0ms and in memory beating 86% + solutions.
Wrote last break line to escape unwanted iterations.
"""