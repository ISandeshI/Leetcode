# 5. Longest Palindromic Substring
# 5. Longest Palindromic Substring
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        longest = 1

        def expand(left, right):
            nonlocal start, longest
            currLength = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                longest = max(longest, currLength)
                if longest == currLength:
                    start = left

                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            # for odd length palindrome, let's start at same character
            
            expand(i, i + 1)
            # for even length palindrome, let's start at character and next to it.

        return s[start:start + longest]
            





"""
In my whole life i have wondered how to find a common longest pattern in given data. This is same.
For me it is hardest problem. I give it a thought and gave up. Used chatgpt and solved it.
It runs in 415ms and beats only 37% + solutions. best solution has 52ms of runtime.

initialy i got out of range error for following line because of python's left to right checking approach.
while s[left] == s[right] and left >= 0 and right < len(s):
so i reordered it into above.

Approach is following:
A palindrome expands symmetrically from its center.

There are 2 types of centers:
1. Odd length → "aba" (center at one character)
2. Even length → "abba" (center between two characters)

We expand from each center and keep track of the longest palindrome found.
"""