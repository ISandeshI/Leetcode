# 645. Set Mismatch
# Easy
# Topics
# premium lock icon
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map1 = Counter(nums)
        last = len(nums)
        middle = 0
        if last % 2 == 1:
            middle = (1 + last) // 2
        
        actualSum = (1 + last) * (last // 2) + middle
        sumNow = sum(nums)

        for num in map1:
            if map1[num] == 2:
                duplicateInt = num
                break

        difference = actualSum - sumNow
        missingInt = duplicateInt + difference

        return [duplicateInt, missingInt]


"""
this has runtime of 3ms beating 97%+ solutions and beats only 32% + solutions in memory.
I knew some maths and used the logic. some of them used pretty simple logic like:
creating array noting count of integers in it's index place, the one which has 2 it is duplicate and the one 
which has 0 is missing

code:

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        freq = [0] * (len(nums) + 1)

        for num in nums:
            freq[num] += 1

        duplicate = -1
        missing = -1

        for i in range(1, len(freq)):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i

        return [duplicate, missing]

"""