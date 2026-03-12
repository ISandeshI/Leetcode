# 859. Buddy Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

# Example 1:

# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Example 2:

# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
# Example 3:

# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

# Constraints:

# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.

from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        sFirst = ""
        sSecond = ""
        secondCheck = ""

        if s[:] == goal[:]:
            return len(set(s)) < len(s)
        
        # for edge cases where both s and goal are same also at least one character has to be repeated
        # ex. s=aab goal = aab
        # we can swap aa and result is True
        # but if s= ab and goal = ab
        # then swapping won't achieve anything.
        # To check that at least one character is repeating we have to check it with set(s)

        elif len(s) == len(goal) and Counter(s) == Counter(goal):
            for i in range(len(s)):
                if s[i] != goal[i] and not sFirst:
                    sFirst = s[i]
                    sSecond = goal[i]

                elif s[i] != goal[i] and not secondCheck:
                    if s[i] != sSecond or goal[i] != sFirst:
                        return False
                    secondCheck = "Yes"

                elif s[i] != goal[i] and secondCheck:
                    return False

        if sFirst and secondCheck:
            return True
        else:
            return False
        


"""
This is an over engineered answer. Runtime of 3ms (most have 0ms) and in memory beating only 63% + solutions.
Following is much simpler solution:

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]


"""