# 744. Find Smallest Letter Greater Than Target
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# Example 3:

# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 

# Constraints:

# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetAscii = ord(target) - ord('a')
        if (ord(letters[-1]) - ord('a')) <= targetAscii:
            return letters[0]

        for char in letters:
            currentAscii = ord(char) - ord('a')
            if currentAscii > targetAscii:
                return char
            

"""
Solved in first attempt without looking at any external help.
This runs in 1ms but beats 93% + solutions in  memory.

In python you do not have to convert chars in ASCII( ordinal) value for comparison
You can directly check if char1 < char2. Python converts its length internaly.
for char in letters:
    if char > target:
        return char
return letters[0]

that's the simple code. this runs in 0ms but it only beats 53% + solutions in memory.
"""