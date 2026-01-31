# 387. First Unique Character in a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
 
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str):

        map = Counter(s)
        min1 = len(s)
        for key in map:
            if map[key] == 1:
                min1 = min(min1, s.find(key))
        
        if min1 == len(s):
            return -1
        
        return min1


"""
This took 19ms of runtime still beats 99% other solutions.
"""