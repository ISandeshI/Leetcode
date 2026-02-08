# 485. Max Consecutive Ones
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]):
        maxLength = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > maxLength:
                    maxLength = count
            else:
                count = 0

        return maxLength
    

""" Even before run i knew this was never going to run efficiently. This code runs in 15ms.
Following was my first approach but if longest 1s appeared in last chunk then it never counts them.
So, i changed it to above 

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > maxLength:
                    maxLength = count
                
                count = 0

"""