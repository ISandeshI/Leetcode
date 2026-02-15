# 10. Regular Expression Matching
# Hard
# Topics
# premium lock icon
# Companies
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            # If result already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is exhausted
            if j == len(p):
                return i == len(s)

            # Check first character match
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # If next char is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two choices:
                # 1. Skip "x*"
                # 2. Use "x*" if first character matches
                ans = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                # Normal character match
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

"""
This program runs in 4ms and beats 78% of solutions.
This is AI generated solution. I am too dumb to even understand explaination of this solution.
This is the problem you solve for getting hired at google. The core R&D people who are genius only they 
can solve this. One day if you become sudar pichai, before hiring any developer for R&D division, give them 
this problem and check for their credebility.

https://www.youtube.com/watch?v=HAA8mgxlov8
Watch this for most simple clarifications

GUIDE:
This is part of DP (Dynamic programing). Start from small like
fib series
climbing staircase...

gradualy you will build an approach for DP. Then get your hands on this problem.
"""