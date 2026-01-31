# 191. Number of 1 Bits
# Easy
# Topics
# premium lock icon
# Companies
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def hammingWeight(self, n: int):
    # Basicaly we have to return count of 1's in given number's binary version
        bin1 = bin(n)[2:]
        return bin1.count('1')
    

"""
This is best solutin with 0ms runtime. I know i have used readymade function bin() but
in previous problem i have implemented binary conversion manually.
So here i am using bin() function to convert integer to binary string and then using
count() function to count number of 1's in that string.
I made some silly mistakes. bin() always returns a string.
So when i tried searching for integer 1 in string it returned 0.
you have to provide '1' in count function to get correct result.
my previuos version was:
return bin1String.count(1)

here is the corrected version:
return bin1String.count('1')

"""