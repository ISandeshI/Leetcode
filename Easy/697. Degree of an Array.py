# 697. Degree of an Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        map1 = Counter(nums)
        degreeCount = 0
        intWithHighestDegree = []

        for key, value in map1.items():
            if value == degreeCount:
                intWithHighestDegree.append(key)
            elif value > degreeCount:
                intWithHighestDegree = [key]
                degreeCount = value

        if degreeCount == 1:
            return 1
        else:
            minLegth = float('inf')

            for int in intWithHighestDegree:
                firstOccurence, LastOccurence = -1, 0
                for i in range(len(nums)):
                    if firstOccurence == -1 and nums[i] == int:
                        firstOccurence = i

                    elif nums[i] == int:
                        LastOccurence = i
                lenght = LastOccurence - firstOccurence + 1
                minLegth = min(minLegth, lenght)

        return minLegth


"""
This solution has runtime of 15ms which is highest and beats 88% + solutions. Top is with 6ms.
many others have 20ms of runtime.
This problem should have been in medium.
"""
        
            
