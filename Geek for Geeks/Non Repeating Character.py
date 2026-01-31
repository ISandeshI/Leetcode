# Non Repeating Character
# Difficulty: EasyAccuracy: 40.43%Submissions: 328K+Points: 2Average Time: 30m
# Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string, 'f' is the first character in the string which does not repeat.
# Input: s = "racecar"
# Output: 'e'
# Explanation: In the given string, 'e' is the only character in the string which does not repeat.
# Input: s = "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.
# Constraints:
# 1 ≤ s.size() ≤ 105

from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        
        map1 = Counter(s)
        map2 = filter(lambda x: map1[x] ==1,map1)
        map2 = list(map2)
        if map2:
            for i, val in enumerate(s):
                if val in map2:
                    return val


        return "$"
    

    """
    initially i made mistake in lambda i wrote
    map2 = filter(lambda x: x == 1, map1)
    which is wrong because x is key here not value
    so i corrected it to above version.

    """