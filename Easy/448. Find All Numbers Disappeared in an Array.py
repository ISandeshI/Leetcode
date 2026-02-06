# 448. Find All Numbers Disappeared in an Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        set1 = set(nums)
        list1 = []
        for i in range (1, len(nums) + 1):
            if i not in set1:
                list1.append(i)
        return list1
    
"""
There are many ways to solve this. Above solution runs in 27ms and beats 59% + solutions out there.
Following was best one line solution, which usses set A - set B concept:
return list(set(range(1,len(nums)+1))-set(nums))

-------------------------------------------------------------------
Following is an approach to solve follow up question:

For each value x in the array:
Mark the element at index x - 1 as negative
If it's already negative, leave it

After this pass:
Any index i where nums[i] is positive means number i + 1 was missing

Code:

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark numbers as visited
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Find missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result


"""