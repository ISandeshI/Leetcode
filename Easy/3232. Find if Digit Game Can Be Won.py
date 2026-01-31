# 3232. Find if Digit Game Can Be Won
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of positive integers nums.

# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

# Return true if Alice can win this game, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,10]

# Output: false

# Explanation:

# Alice cannot win by choosing either single-digit or double-digit numbers.

# Example 2:

# Input: nums = [1,2,3,4,5,14]

# Output: true

# Explanation:

# Alice can win by choosing single-digit numbers which have a sum equal to 15.

# Example 3:

# Input: nums = [5,5,5,25]

# Output: true

# Explanation:

# Alice can win by choosing double-digit numbers which have a sum equal to 25.

 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 99

class Solution:
    def canAliceWin(self, nums: List[int]):
        count1, count2 = 0, 0

        for i in range(len(nums)):
            if nums[i] < 10:
                count1 += nums[i]
            else:
                count2 += nums[i]

        return not count1 == count2
    
"""
It is strictly told either sum of single digits or double digits has to be greater than
other sum. means we can return false only if sum of both cases is equal.
remember the constraint is range of integers is less than 100.
Thats why we never cosidered the possibility of digits more than 100
"""
