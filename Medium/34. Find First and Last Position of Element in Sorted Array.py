# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int):
        count = nums.count(target)
        left, right = 0, len(nums) - 1
        if count:
            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return [left, left + count -1]
        
        else:
            return [-1, -1]
        
"""
This runs in 0ms. Remember this unique case of bs.
We have to check first occurence and may be others also in sorted array.
here two important things happens.
while left < right
and right do not decrease. it stays with mid.
And the moment we found our first occurece with left, We keep our left
there only.
In the end we return left.
"""