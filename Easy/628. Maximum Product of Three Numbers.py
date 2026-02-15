# 628. Maximum Product of Three Numbers
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
    
"""
This problem look simple but it should be in medium. It is tricky one.
Above solution is worse with 27ms of runtime and only beats 15%.
It has big solution:

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for n in nums:
            # Track top 3 maximums
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n

            # Track bottom 2 minimums
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)

"""