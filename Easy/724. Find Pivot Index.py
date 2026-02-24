# 724. Find Pivot Index
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
# Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        center = 0

        while center < len(nums):
            rightSum -= nums[center]
            if center > 0:
                leftSum += nums[center - 1]
            if rightSum == leftSum:
                return center
            
            center += 1
        
        return -1


"""
Above code runs in 8ms and beats 40% + solutions and beats 63% + solutions in memory.
I tried running following lines after line number 59, to end loop early and save time, but it is not possible because there 
are some special cases which involves negaticve numbers and then calculations became irrelavants:

            elif leftSum > rightSum > 0:
                return -1
--------------------------------------------------------------

Above code can be reduced to following:

        while center < len(nums):
            rightSum -= nums[center]
            if rightSum == leftSum:
                return center
            leftSum += nums[center]
            center += 1
        
        return -1

"""