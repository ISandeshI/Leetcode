# 409. Longest Palindrome
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        centralCount = 0
        repeatCount = 0
        if len(s) % 2 == 1:
            centralCount = 1
        map1 = Counter(s)

        for key, value in map1.items():
            if value % 2 == 1:
                centralCount = 1
            
            if value > 1:
                if value % 2 == 1:
                    repeatCount += value - 1
                else:
                    repeatCount += value

        return centralCount + repeatCount
    

"""
This runs in 0ms and beats only 43% in memory.
Logic is simple, count repeated characters in pairs and if there is odd count we can place it in center.
line 34-35 is useless, because we are checking each individual for central count.
"""