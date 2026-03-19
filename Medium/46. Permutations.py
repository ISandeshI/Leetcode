# 46. Permutations
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)

        def recursion(currentIndex, listTillNow):
            if len(listTillNow) == length:
                ans.append(listTillNow.copy())
                return
            
            for i in range(length):
                if nums[i] in listTillNow:
                    continue
                listTillNow.append(nums[i])
                recursion(i + 1, listTillNow)
                listTillNow.pop()

        recursion(0, [])
        return ans
    
"""
Runtime 3ms beating only 30% + solutions and in memory beating 56% + solutions.
each time we are going through recursion again we check for each element again if it is there in 
current list or not. only if not present then just include it in the list.

Line 41 - 45 can be written as, and we get runtime 0ms:

                if nums[i] not in listTillNow:
                    listTillNow.append(nums[i])
                    recursion(i + 1, listTillNow)
                    listTillNow.pop()
"""