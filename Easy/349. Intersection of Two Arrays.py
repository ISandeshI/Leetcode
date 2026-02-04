# 349. Intersection of Two Arrays
# Easy
# Topics
# premium lock icon
# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        return list(set(nums1).intersection(set(nums2)))
    
"""
I have intentionaly used readymade function over here. it runs in 1 ms.
90%+ have 0ms runtime. Following is an alternate version with 7ms runtime:

list1 = []
for i in nums2:
    if i in nums1 and i not in list1:
        list1.append(i)
return list1

----------------------------------------------------------------------------

Intersection of A and B can be written as:
A - (A - B)
code: return list(set(nums1)-(set(nums1) - set(nums2)))

For sets, the - operator means:

Set difference, elements that are in A but NOT in B
A = {1, 2, 3, 4}
B = {3, 4, 5}

A - B
✅ Result: {1, 2}
"""