# 494. Target Sum
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(currentIndex, sumTillNow):
            if (currentIndex, sumTillNow) in dp:
                return dp[(currentIndex, sumTillNow)]
            
            if currentIndex == len(nums):
                if sumTillNow == target:
                    return 1
                return 0
            
            dp[(currentIndex, sumTillNow)] = (backtrack(currentIndex + 1, sumTillNow + nums[currentIndex]) + backtrack(currentIndex + 1, sumTillNow - nums[currentIndex]))

            return dp[(currentIndex, sumTillNow)]

        return backtrack(0, 0)
        
    
"""

Runtime 184ms Beating 17.26% + solutions and in memory beating 13.42% + solutions.

1. Initialy i wrote:

            backtrack(currentIndex + 1, sumTillNow += nums[currentIndex])
            backtrack(currentIndex + 1, sumTillNow -= nums[currentIndex])

this gave an error because python does not allow assignment inside function call.
So i corrected to above

2. Because Python treats "count" as a local variable unless declared otherwise.
So nonlocal word was declared at top.

3. with pure backtracking we got TLE.
this problem needs DP solution.
Following was my initial code:

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def backtrack(currentIndex, sumTillNow):
            nonlocal count
            if currentIndex == len(nums):
                if sumTillNow == target:
                    count += 1
                return
            
            backtrack(currentIndex + 1, sumTillNow + nums[currentIndex])
            backtrack(currentIndex + 1, sumTillNow - nums[currentIndex])


        backtrack(0, 0)
        return count
"""