# 190. Reverse Bits
# Easy
# Topics
# premium lock icon
# Companies
# Reverse bits of a given 32 bits signed integer.

 

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
 

# Constraints:

# 0 <= n <= 231 - 2
# n is even.

class Solution:
    def reverseBits(self, n: int):
        quotient = n
        reminder = 0
        count = 0
        i, power = 31, 31
        bin1 = [0] * 32
        
        while quotient > 0:
            reminder = quotient % 2
            quotient //= 2
            bin1[i] = reminder
            i -= 1

        bin2 = bin1 [::-1]

        for j in range(32):
            count += bin2[j] * (2**power)
            power -= 1

        return count
    

"""
I tried solving this by basic knowledge of converting decimal to binary and vice versa.
This is not the most optimal solution but it works fine. It has 42ms runtime.
We could have used readymade functions to convert decimal to binary and vice versa.

Also i make mistake of power operator, used ^ instead of ** initially.

"""

