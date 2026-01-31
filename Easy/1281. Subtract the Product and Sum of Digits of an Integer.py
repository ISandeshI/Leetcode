# 1281. Subtract the Product and Sum of Digits of an Integer
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 

# Constraints:

# 1 <= n <= 10^5

class Solution:
    def subtractProductAndSum(self, n: int):
        product = 1
        sum = 0
        list1 = []

        while n > 0:
            remainder = n % 10
            n //= 10
            list1.append(remainder)

        for i in list1:
            product *= i
            sum += i

        return (product - sum)
    
"""
Never needed extra for loop, it caused us extra runtime. Above solution works in 4ms runtime.
we could have just wrote:
class Solution:
    def subtractProductAndSum(self, n: int):
        product = 1
        sum = 0

        while n > 0:
            remainder = n % 10
            n //= 10
            product *= remainder
            sum += remainder

        return (product - sum)

"""