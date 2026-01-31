# 2529. Maximum Count of Positive Integer and Negative Integer
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

# Constraints:

# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.

class Solution:
    def maximumCount(self, nums: List[int]):
        negCount = list(filter(lambda x: x<0, nums))
        posCount = list(filter(lambda x: x>0, nums))

        return max(len(negCount),len(posCount))
    

"""
Solved this and it has 4ms runtime, still 4th solution.
the basic solution of counting positive and negative numbers
is still among the top solutions.
Although both has same time complexity O(n), this one uses filter.

Great programmer do not overcomplicate things.

Following is the binary search solution with O(log n) time complexity:
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Find first index where value >= 0
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        first_non_negative = left

        # Find first index where value > 0
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        first_positive = left

        negative_count = first_non_negative
        positive_count = n - first_positive

        return max(negative_count, positive_count)

"""
     




