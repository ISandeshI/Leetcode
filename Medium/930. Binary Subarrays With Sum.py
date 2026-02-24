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
        def atMost(k):
            left = 0
            count = 0
            currTotal = 0
            
            for right in range(len(nums)):
                currTotal += nums[right]
                
                while currTotal > k:
                    currTotal -= nums[left]
                    left += 1
                
                count += right - left + 1
            
            return count
        
        if goal < 0:
            return 0
        
        return atMost(goal) - atMost(goal - 1)




"""
This is an AI generated code and i can't explain this.
watch this for better explaination:
https://www.youtube.com/watch?v=w_lNKXAEWdM

example: to find result upto 2
find set of 0,1,2 and set of 0,1
then if you subtract them then you will get result of 2
that's the reason behind last line in above code.

above question is tricky, if we encounter continous 0s, and even if we move left, sum is not affected.
so we actualy get more combinations. now the solution is count each time if current sum is less than 
equal to goal, if yes then count the length of current subarray to count.
in the end number of such conditions added will give us our result.

How exactly this algorithm works i don't know
"""