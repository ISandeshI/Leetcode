# 242. Valid Anagram
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str):
        map1 = Counter(s)        
        map2 = Counter(t)        

        return map1 == map2
    

"""
There are many simple mehods like cheking counter of both s & t is equal or not, sorted s & t equal or not

Anagrams cannot be solved using XOR because XOR does not preserve character frequencies.
Any XOR-based solution will fail due to collisions.
Initially i i thought s+t but it has some cases where it fails
: s = "a", t = "abb"
So answer will be true by code but it's not an Anagram
Code was:

        ans = 0
        for i in s + t:
            ans ^= ord(i)

        return not ans

Anagrams need frequency, not math tricks
Anagrams require checking:

count('a'), count('b'), ..., count('z')

That's 26 independent values, not 1.

Reducing 26 dimensions → 1 dimension
= information loss ❌
"""