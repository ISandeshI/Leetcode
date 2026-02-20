# 930. Binary Subarrays With Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - goal in freq:
                count += freq[prefix_sum - goal]
            
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        
        return count





"""
This is an AI generated code and i can't explain this.
above question is tricky, if we encounter continous 0s, and even if we move left, sum is not affected.
so we actualy get more combinations. now the solution is count each time if current sum is less than 
equal to goal, if yes then count the length of current subarray to count.
in the end number of such conditions added will give us our result.

How exactly this algorithm works i don't know
"""