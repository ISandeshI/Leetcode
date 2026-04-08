# 491. Non-decreasing Subsequences
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:

# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
 

# Constraints:

# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        set1 = set()
        n = len(nums)

        def backtrack(currentIndex, currentArray):     
            if len(currentArray) > 1:
                t = tuple(currentArray)
                if t not in set1:
                    set1.add(t)
                    ans.append(currentArray.copy())
            
            for i in range(currentIndex,n):
                if not currentArray or currentArray[-1] <= nums[i]:
                    currentArray.append(nums[i])
                    backtrack(i + 1, currentArray)
                    currentArray.pop()

        backtrack(0, [])
        return ans
    
"""
Runtime 23ms beating only 42% solutions and in memory beating only 5% + solutions.
Like this or not but i am dependent on AI heavily.
Lists are unhashable, so you cannot store list into set
You must convert to tuple, that's what we did in line 34-36.
"""