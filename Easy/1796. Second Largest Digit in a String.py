# 1796. Second Largest Digit in a String
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.

 

# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters and digits.

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = "0123456789"
        firstHigh = secondHigh = -1

        for char in s:
            if char in digits:
                num = int(char)
                if num > firstHigh:
                    secondHigh = firstHigh
                    firstHigh = num
                elif num < firstHigh and num > secondHigh:
                    secondHigh = num

        return secondHigh

"""
Runtime is 3ms beating 77% + solutions and in memory beating 95% + solutions.

Following are few changes to make runtime 0ms:

class Solution:
    def secondHighest(self, s: str) -> int:
        firstHigh = secondHigh = -1

        for char in s:
            if char.isdigit():
                num = int(char)
                if num > firstHigh:
                    secondHigh = firstHigh
                    firstHigh = num
                elif num < firstHigh and num > secondHigh:
                    secondHigh = num

        return secondHigh
"""