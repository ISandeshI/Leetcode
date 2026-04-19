# 1790. Check if One String Swap Can Make Strings Equal
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
 

# Constraints:

# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1FirstFound = s2FirstFound = ""
        diffCharCount = 0

        for i in range(n):
            if s2[i] != s1[i]:
                if not s1FirstFound:
                    s1FirstFound = s1[i]
                    s2FirstFound = s2[i]
                    diffCharCount += 1
                else:
                    if s1FirstFound == s2[i] and s2FirstFound == s1[i] and diffCharCount == 1:
                        diffCharCount += 1
                    else:
                        return False
                    
        return diffCharCount == 0 or diffCharCount ==2
    
"""
Runtime is 0ms and in memory beating 72% + solutions.
This problem looked simple but it took me around half an hour to solve this.
I don't know why. Following is simplest code:

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differ=[]
        
        for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    differ.append(i)
        if len(differ) == 0:
            return True

        if len(differ)==2:
            i,j=differ
            return s1[i]==s2[j] and s1[j]==s2[i]
        return False
"""