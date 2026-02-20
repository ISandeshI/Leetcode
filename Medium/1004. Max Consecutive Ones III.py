# 1004. Max Consecutive Ones III
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


"""
this is AI generated code. runs in 65ms and beats 46% + solutions

folowing got TLE:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLength = 0
        
        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1
                    
                if zeros > k:
                    break
                    
                maxLength = max(maxLength, j - i + 1)
                
        return maxLength
"""

