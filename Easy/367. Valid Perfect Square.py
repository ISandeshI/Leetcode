# 367. Valid Perfect Square
# Easy
# Topics
# premium lock icon
# Companies
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

# Constraints:

# 1 <= num <= 231 - 1

class Solution:
    def isPerfectSquare(self, num: int):

        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if (mid * mid) > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
    

"""
Above solution runs in 0ms. beating 75% other solutions
Initialy i wrote wrong logic at two spaces:

1.
            if (mid * mid) > right:
                right = mid - 1

so i have to check if mid * mid > num
After comparing it with given number we have to decide remaining operations

2. i wrote:
while left < right:

instead it should be 
while left <= right:

We use while left <= right because left == right is still a valid candidate that must be checked.
Using left < right skips the last possible value.

if we are given only one value like 1. in such cases above code is perfect.

Following was my extra line to check this condition.
        if num == 1:
            return True

Now it's not needed


"""