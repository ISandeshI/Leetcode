# 830. Positions of Large Groups
# Easy
# Topics
# premium lock icon
# Companies
# In a string s of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in increasing order by start index.

 

# Example 1:

# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:

# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:

# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".
 

# Constraints:

# 1 <= s.length <= 1000
# s contains lowercase English letters only.

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        individualCount = 0
        left = 0

        for right in range(len(s)):
            if s[left] == s[right]:
                individualCount += 1
                if (right + 1) < len(s) and s[left] != s[right + 1] and individualCount > 2:
                    result.append([left,right])
                elif (right + 1) == len(s) and individualCount > 2:
                    result.append([left,right])

            else:
                left = right
                individualCount = 1

        return result
    
"""
Runtime 3ms beating only 32% + solurtions and in memory beating 61% + solutions.
This answer has so many if else with multiple conditions to check in deeper levels; making it slower.
Don't refer this solution because many of them have 0ms runtime. I found following solution with 
very simplistic approach to minimalise condition checking.
Code:

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0
        n = len(s)
        while start < n:
            end = start
            while end < n and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                result.append([start, end - 1])
            start = end
        return result


"""