# 643. Maximum Average Subarray I
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        for i in range(k):
            sum1 += nums[i]
            
        maxWindow = sum1

        for i in range(1, len(nums) - k + 1):
            sum1 -= nums[i - 1]
            sum1 += nums[i + k - 1]

            maxWindow = max(maxWindow, sum1)

        return maxWindow / k

"""
This is an awful solution that runs in 69ms and beats only 58% + solutions.
This is obvioulsy most simple sliding window problem. Initialy i used following code which got TLE
because sum() function takes much time in each loop.

        maxTotal = float('-inf')
        for i in range(0, len(nums) - k - 1):
            maxTotal = max(maxTotal, sum(nums[i:i + k]))

        return maxTotal / k
"""