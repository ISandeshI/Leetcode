# 680. Valid Palindrome II
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True
            
        low, high = 0, len(s) - 1

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1

            else:
                return is_palindrome(low + 1, high) or is_palindrome(low, high - 1)
            
        return True
    

        

"""
Used chatgpt and still it has runtime of 61ms and beats 46% solutions and beats 55% + solutions in memory.
You are allowed to delete at most one character.
So:
Traverse with two pointers
On first mismatch:
Either skip left character
Or skip right character
Check if either remaining substring is a palindrome
Even if string was already palindrome and we can delete one character we can still get palindrome in one case


initial approach was to check everything but for large inputs it got TLE:
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            s2 = s
            s2 = s[:i] + s[i + 1:]
            if s2[:] == s2[::-1]:
                return True
            
        else:
            return False
"""