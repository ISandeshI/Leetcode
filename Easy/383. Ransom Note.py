# 383. Ransom Note
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        map1 = Counter(magazine)
        set1 = set(ransomNote)

        for char in set1:
            if ransomNote.count(char) > map1[char]:
                return False
            
        return True


"""
I made this overcopmlicated. This has runtime of 64ms.
it has really simple solution, check count of each char from ransom should be less than or equal to 
count of same char in magzine. You do not need counter everytime. start thinking simply.
Do not heavily rely on counter. Also counter consumes more runtime.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True
"""