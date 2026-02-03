# 228. Summary Ranges
# Easy
# Topics
# premium lock icon
# Companies
# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.

class Solution:
    def summaryRanges(self, nums: List[int]):
        list2 = []
        
        if len(nums):
            str1 = "" + str(nums[0])
            b = None
            for i in range(1, len(nums)):
                if (nums[i - 1] + 1) == nums[i]:
                    b = nums[i]
                else:
                    if b == None:
                        list2.append(str1)
                    else:
                        list2.append(str1 + "->" + str(b))
                    
                    str1 = "" + str(nums[i])
                    b = None
            
            if b is None:
                list2.append(str1)
            else:
                list2.append(str1 + "->" + str(b))

        return list2
            

"""
Runs in 0ms. Made a lot of mistakes. My last loop did not append list.
So i have to write same code even after loop ends for one more time.
This question has unique condition, if given list is empty, that's why i have to check
for that condition aslo. I overcomplicated this, could have used two pointers approach.

Following is one of simplest code:

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")

            i += 1

        return res

"""