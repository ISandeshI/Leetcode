# 205. Isomorphic Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str):
        sTOt = {}
        tTOs = {}

        if len(s) == len(t):
            for charIns, charInt in zip(s,t):
                if charIns in sTOt and sTOt[charIns] != charInt:
                    return False
                
                if charInt in tTOs and tTOs[charInt] != charIns:
                    return False
                
                sTOt[charIns] = charInt
                tTOs[charInt] = charIns

            return True


        else:
            return False

    



""""
I tried solving this using replace, slicing and god knows how many different ways.
But i failed. because this question has one solution map each character to other and then check it.
Above approach is simple map everything to each other in different dictionaries.
if there are multiple mappings then return False.
Yet this is worse answer because it has 7ms of runtime

I saw best solution, obviously someone has used great logical around it:

def isIsomorphic(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

That's it. creating a set of s, t and a set of "map of s to t"

length of all three has to equal otherwise it is false.
As we know set gives you only unique instances.

And obviously it has 0ms runtime.

"""
