# 905. Sort Array By Parity
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            while nums[i] % 2 == 0 and i < j:
                i += 1
            
            while nums[j] % 2 == 1 and i < j:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        return nums
    
"""
Runtime 0ms and in memory beating 59% + solutions.
I run this program on purpose so there won't be need of another space.
we did number exchange inside the array itself.
"""