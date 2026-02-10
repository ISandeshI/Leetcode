# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        i, j = 0, 1

        if len(s):
            set1.add(s[0])
            count = 1
            while j < len(s):
                if s[j] not in set1:
                    set1.add(s[j])
                    j += 1
                    count = max(count, len(set1))

                else:
                    set1.discard(s[i])
                    i += 1
            return count
        else:
            return 0
            
"""
This runs in 14ms and beats 40% +, and in memory it beats 43% +.
kept the track of two pointers i and j. if duplicate from set is not found then move j
otherwise delete character of i from set move it to right but at this time do not move j.
at any given condition either j is moving or i.
"""