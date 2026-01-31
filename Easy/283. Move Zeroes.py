# 283. Move Zeroes
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def moveZeroes(self, nums: List[int]):
        i = len(nums) - 1
        count = nums.count(0)

        while i >= 0:
            if nums[i] == 0:
                nums.pop(i)

            i -= 1

        for i in range(count):
            nums.append(0)
         

"""
I am officially an IDIOT. This is the simplest problem ever and I overcomplicated it so much.
It took me 3 days of thinking. In the end i remember a different question where attacking from
the end don't chage indexes of previous elements. Although i have made logical error like
      while i > 0:
      And 
      while i < 0:
      
This solution has 8ms runtime and beats 100% of submissions.

Although there is a different approach where we can use two pointers to swap elements in place
without using pop and append which might be costly in terms of time complexity.

i = 0  # position for next non-zero

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


from the beginning i stays at position where if 0 is found.
j moves forward if non zero is found.
Then both make swap.

But the key pont is both moves forward at same pace and index until they find 
first zero for i and first non zero for j.

"""

            

            

 

            


        
