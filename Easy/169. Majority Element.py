# 169. Majority Element
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]):
        count = Counter(nums)
        result = filter(lambda x: count[x] > (len(nums)/2) , count)
        return list(result)[0]
"""
Above solution is among top 3 with 3ms runtime.


my previous answer was:
        result = filter(lambda x: count[x] > (len(nums)/2) , count)
        return result[0]

        raises:
TypeError: 'filter' object is not subscriptable

In Python 3, filter() returns a filter object (iterator), not a list.

So we can either write following way:
        result = list(filter(lambda x: count[x] > (len(nums)/2) , count))
        return result[0]

        or

        result = filter(lambda x: count[x] > (len(nums)/2) , count)
        return list(result)[0]

----------------------------------------------------------------------------------

Perfect choice — Boyer–Moore Majority Vote Algorithm

Core Idea (Intuition):

Think of it like canceling votes:

Majority element has more votes than all others combined
Pair one majority vote with one non-majority vote → they cancel out
The majority element cannot be fully canceled

Step-by-Step Logic:

We maintain:
candidate → potential majority element
count → vote balance

Rules:
If count == 0 → pick current element as candidate
If current element == candidate → count += 1
Else → count -= 1


Code:

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


"""