# 717. 1-bit and 2-bit Characters
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# We have two special characters:

# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

# Example 1:

# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:

# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ans = True
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                ans = False

            else:
                ans = True
                i += 1

        return ans
    
"""
This runs in 0ms and beats only 15% + in memory.
There is no shortcut in checking just last few indexes. You have to traverse through array and check 
for last index.
"""