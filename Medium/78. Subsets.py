# 78. Subsets
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursion(currentIndex, currentList):
            if currentIndex == len(nums):
                ans.append(currentList.copy())
                return
            
            currentList.append(nums[currentIndex])
            recursion(currentIndex + 1, currentList)
            currentList.pop()
            recursion(currentIndex + 1, currentList)
            
        recursion(0, [])
        return ans
    

"""
Runtime 0ms and in memory beating 59% + solutions.
Initialy recursion and backtracking was way too hard for me. But with practise and countless youtube 
tutorials on this topic made this easy for me.
"""