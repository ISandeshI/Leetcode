# 162. Find Peak Element
# Medium
# Topics
# premium lock icon
# Companies
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low
    
"""
Obviously i couldn't solve this. This was simple task but the problem mentioned it has to solve in O(log n).
So key idea is when you get middle. check if it is greater than it's right then there is at least 
higher side on left for sure. based on this we move our right to mid itself. Otherwise move left to mid + 1.
because mid is itself not greater then go to right by one.

remember in BS there are mostly two patterns:
1. while low < high:
based on condition at bottom: high = mid and low = mid + 1 

2. while low <= high:
based on condition at bottom: high = mid - 1 and low = mid + 1

"""