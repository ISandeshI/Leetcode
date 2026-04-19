# 1624. Largest Substring Between Two Equal Characters
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
 

# Constraints:

# 1 <= s.length <= 300
# s contains only lowercase English letters.

from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        countHashMap = Counter(s)
        maxGap = float("-inf")
        for key in countHashMap:
            if countHashMap[key] > 1:
                gapBetTwoSimilar = s.rfind(key) - s.find(key) - 1
                maxGap = max(maxGap, gapBetTwoSimilar)

        return maxGap
    
"""
Runtime is 2ms beating only 36% + solutions and in memory beating only 62% + solutions.
most of the solutions have 0ms runtime. Following is solution without Counter:

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1
        
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            else:
                ans = max(ans, i - first[ch] - 1)
        
        return ans
"""