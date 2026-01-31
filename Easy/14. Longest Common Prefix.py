# 14. Longest Common Prefix
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        str1 = ""
        minLength = len(strs[0])
        for char in strs:
            minLength = min(minLength,len(char))

        j = 0

        while minLength > 0:
            for i in range(len(strs) - 1):
                if strs[i][j] == strs[i + 1][j]:
                    pass
                else:
                    return str1
            
            str1 += strs[0][j: j + 1]
            j += 1
            
            minLength -= 1

        return str1
    

"""
This runs in 0ms. Initially i made mistake of minLength = 0
So it was not entering while loop. I corrected it to minLength = len(strs[0])
Above code can be shorten we can see there is pass statement with if condition.
we can directly use if not condition and return str1:
        while j < minLength:
            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i + 1][j]:
                    return str1

            str1 += strs[0][j]
            j += 1

"""