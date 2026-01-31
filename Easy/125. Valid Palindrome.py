# 125. Valid Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str):
        result = "".join(ch for ch in s if ch.isalnum())
        result = result.lower()
      
        if result == result[::-1]:
            return True
        else:
            return False
        

"""
i made a mistake in the previous submission
i wrote result.lower() but did not assign it back to result.

Strings are immutable in Python.
lower() does not modify result

so i corrected it by assigning it back to result
result = result.lower()

"""