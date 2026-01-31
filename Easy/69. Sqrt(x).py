# 69. Sqrt(x)
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1


class Solution:
    def mySqrt(self, x: int):
        left, right = 0, x
        half = (left + right) // 2
        while left <= right:
            if half * half == x:
                return half
            if half * half < x:
                left = half + 1
            else:
                right = half - 1

            half = (left + right) // 2

        return right
    

"""
can't believe I solved this using binary search after so long
there are better solutions available to find square root like Newton's method
def newton_sqrt_fast(n, iterations=10):
    x = n
    for _ in range(iterations):
        x = 0.5 * (x + n / x)
    return x

still on leetcode this solution in number one in performance with 10ms runtime.
"""