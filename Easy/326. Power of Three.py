# 326. Power of Three
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

import math
class Solution:
    def isPowerOfThree(self, n: int):
        if n > 0:
            ans = math.log(n) / math.log(3)
            return abs(ans - round(ans)) < 1e-10
        return False



"""
This code runs in 7ms.

you can write following line as well:
ans = math.log(n, 3)

I know simple solution of keep finding remainder by 3 in loop. This method has 0ms runtime.
But decided to go as per follow up question's approach.
return abs(ans - round(ans)) < 1e-10
I have copied this line from AI.

Following approach is my previous version, which is also correct but it is prone to floating point error.

        if n > 1:
            ans = math.log(n) / math.log(3)
            return ans == round(ans)
        return False

4.999999999999999 ≠ 5
This is a floating-point rounding error, not a logic mistake.
"""