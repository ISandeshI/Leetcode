# 693. Binary Number with Alternating Bits
#     Easy
# Topics
# premium lock icon
# Companies
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str1 = bin(n)[2:]

        for i in range(1, len(str1)):
            if str1[i] == str1[i - 1]:
                return False
        return True


"""
This also runs in 0ms but beats only 26% + solutions in memory.
following is bitwise operation solution:
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0

explaination:
1.(n >> 1)

this shifts bits to right by 1. ex.
n = 5, Binary: 101
Shift right:   -010

2. n ^ (n >> 1)
this will make everything 1s only if given 'n' has all alternating bits.
ex. 101
   ^010
--------------
    111

3. (x + 1) if all are 1s, we get 1 and all 0s ahead, but now length is increased by 1
111+1 = 1000

4. (x & (x + 1)) == 0
and operation will return 0 only if all other bits in previous lenght were 0s
ex. 101
   &000
---------------
    000

if this matches then yes we have everything in alternating bits.

"""