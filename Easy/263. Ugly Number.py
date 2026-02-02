# 263. Ugly Number
# Easy
# Topics
# premium lock icon
# Companies
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1

class Solution:
    def isUgly(self, n: int):
        if n <= 0:
            return False
        
        for factor in (2, 3, 5):
            while (n % factor) == 0:
                n //= factor

        return n == 1


"""
This runs in 0ms. I did check the following concept because i had no idea about solving ugly number using maths.
In above for loop, we provided a tuple of size 3. And one by checked each number for factorization.
Key idea
If a number is ugly, you should be able to keep dividing it by 2, 3, and 5 until it becomes 1.
If anything remains other than 1, then it had some other prime factor → not ugly.
"""