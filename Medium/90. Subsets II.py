# 90. Subsets II
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def recursion(currentIndex, currentList):
            if currentIndex == len(nums):
                ans.append(currentList.copy())
                return
            
            currentList.append(nums[currentIndex])
            recursion(currentIndex + 1, currentList)
            currentList.pop()

            while currentIndex < n -1 and nums[currentIndex] == nums[currentIndex + 1]:
                currentIndex += 1

            # skipping all same integer occurences because they have been already covered in previous backtracking
            
            recursion(currentIndex + 1, currentList)
            
        recursion(0, [])
        return ans
    
"""
Runtime 0ms and in memory beating 81% + solutions.

At line 43 i wrote:
            if currentIndex < n - 1 and nums[currentIndex] == nums[currentIndex + 1]:
                return

this is really dumb line. we are kust ignoring all further combinations. Whereas our goal is:
if there is any further duplicates as of current index character, then just skip them.
Remeber one time inclusion is neccessary then once it is included then after removal of current character 
do not check any possibility of same repeating characters ahead. Because that posibility is already covered 
in previous backtracking.
"""