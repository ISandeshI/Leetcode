# 461. Hamming Distance
# Easy
# Topics
# premium lock icon
# Companies
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
 

# Constraints:

# 0 <= x, y <= 231 - 1

class Solution:
    def hammingDistance(self, x: int, y: int):
        z = x ^ y
        return bin(z).count('1')
    
"""
Hamnet distance is how many bits are different. so i XORed given numbers and it will reveal
how many bits are different by giving 1s, Then simply calculate 1's in that string

Above solution runs in 0ms
"""