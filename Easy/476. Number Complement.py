# 476. Number Complement
# Easy
# Topics
# premium lock icon
# Companies
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

 

# Example 1:

# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:

# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

# Constraints:

# 1 <= num < 231

class Solution:
    def findComplement(self, num: int):
        str1 = bin(num)[2:]
        str2 = ""
        for i in str1:
            if i == '0':
                str2 += '1'
            else:
                str2 += '0'
        return int(str2, base= 2)
    
"""
runs in 0ms. I could have converted int to binary and vice versa using maths.
But done this countless times so used readymade functions.
"""