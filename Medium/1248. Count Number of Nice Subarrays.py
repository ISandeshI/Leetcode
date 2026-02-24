# 1248. Count Number of Nice Subarrays
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
 

# Constraints:

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

class Solution:
    def numberOfSubarrays(self, nums, k):
        
        def atMost(k):
            left = 0
            count = 0
            odd_count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMost(k) - atMost(k - 1)
    
"""
Runtime 149ms and beating only 24% + solutions and in memory beating 78% + solutions.
These are all similar questions where right or left cannot be moved based on other's decision.
So there is no perfect flow whether to move right or let, there are all possiblities. And if solved with 
brute force then we ger time complexity of O(n^2). No interviewer wants this.
In such cases we have to use atmost() conditions.
There are all same just inbetween logics get altered based on conditions.
"""