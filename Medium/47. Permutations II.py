# 47. Permutations II
#recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)
        boolArray = [False for _ in range(length)]

        def recursion(currentIndex, listTillNow):
            if len(listTillNow) == length:
                ans.append(listTillNow.copy())
                return
            
            for i in range(length):
                if boolArray[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not boolArray[i - 1]:
                    continue

                boolArray[i] = True
                listTillNow.append(nums[i])
                recursion(i + 1, listTillNow)
                listTillNow.pop()
                boolArray[i] = False

        recursion(0, [])
        return ans
    

"""
Runtime 0ms and in memory beating 44% + solutions.
Approach:
1. keep a track of same length boolean array, initialy set to all values as False.
It indiacates if integers from nums is taken or not.
2. Once everything is included then while removing one by one (backtracking), we have to check if previous 
is same or not. if yes and also is False, meaning it has been tracked already. and there is no point in 
checking same tree outputs. so just skip it.

For more details check following explaination video:
https://www.youtube.com/watch?v=9HTOWRiwYOI

timeline: 31:10 - 44:50
"""