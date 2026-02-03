# 217. Contains Duplicate
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate(self, nums: List[int]):
        set1 = set(nums)
        return len(set1) < len(nums)
    
"""
I just wanted different approach. This is worse performing solutino. It has 19ms runtime.
There are so many approaches like checking count of each character starting from index 0,
if more than 1 then return True.
We could have used counter again.
we could have also wrote:

class Solution:
    def containsDuplicate(self, nums: List[int]):
        return len(set(nums)) < len(nums) 

"""