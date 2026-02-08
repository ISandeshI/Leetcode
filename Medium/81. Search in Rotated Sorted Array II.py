# # 81. Search in Rotated Sorted Array II
# Medium
# Topics
# premium lock icon
# Companies
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104
 

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

# --------------------------------------------------------------------------------------
# this is advance question of 33 question where there are repeated elements

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            elif nums[left] <= nums[mid]: #checking if left side is sorted or not
                if nums[left] <= target < nums[mid]: #if yes then check if target can exist
                    right = mid - 1 #if yes then focus on left section

                else:
                    left = mid + 1 # otherwise focus on right section

            else: #now we know only right side is sorted for sure
                if nums[mid] < target <= nums[right]: #can target lie here
                    left = mid + 1 #if yes then focus on right section
                
                else:
                    right = mid - 1 #otherwise focus on left section

        return False
    
"""
As you know i am worthless piece of humans, and when i copied AI's approach to solve previous problem.
I still have to check approach for current problem when just single difficulty is added.
This code has to run in 0ms and it did.

Here my previous solution stopped at [1,1,0,1,1,1,1]
Because everything, left, right and mid was same so you cannot take any decision.
But there is a solution. If such condition ever happens then shrink left and right by one.
Although we are defeating concept of O(log n) to O(n). But in such case we have this as the best solution.
"""
