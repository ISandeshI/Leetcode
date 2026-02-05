# 414. Third Maximum Number
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution:
    def thirdMax(self, nums: List[int]):
        set1 = set(nums)
        if len(set1) < 3:
            return max(nums)
        highest = max(set1)
        for i in range(2):
            set1.discard(highest)
            highest = max(set1)
        return highest
        
"""
This runs in 4ms, 50% + runs in 0 ms
there so many ways that you can solve this problem. One of the simple way is:

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = list(set(nums))
        n.sort()
        if len(n) <= 2:
            return max(n)
        return n[-3]

"""