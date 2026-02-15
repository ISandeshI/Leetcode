# 1283. Find the Smallest Divisor Given a Threshold
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

 

# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:

# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 106
# nums.length <= threshold <= 106

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            sum1 = 0
            for i in nums:
                sum1 += math.ceil(i / mid)

            if sum1 > threshold:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans


"""
This code has 124ms of runtime and yet it beats 69% + solutions and in memory it is beating 47%+ solutions.
initialy i made conditions wrong where if sum1 > threshold i wrote high = mid -1 and in next line opposite.
Here left is 1 because that will give us highest possible sum which is equivalent to sum of all integers 
from nums. and if we divide from highest of nums then we get lowest sum which is equivalent of 
length of array.
Now we know upper and lower bound then we can solve using BS.

found out interesting thing. if we choose python as a language then we get wrong output for math.ceil()
So we have to move onto latest version python3 on leetcode for running it smoothly.
"""