# 219. Contains Duplicate II
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):

        if len(set(nums)) < len(nums):
                
            map1 = Counter(nums)
            filtered = {k: v for k, v in map1.items() if v > 1}
            
            for key, map1Value in filtered.items():
                lowestDifference = []
                # minimum = 0
                for i, numValue in enumerate(nums):
                    if key == numValue:
                        lowestDifference.append(i)
                        if (len(lowestDifference) == map1Value):
                            break
                
                for j in range(len(lowestDifference) - 1):
                    if (abs(lowestDifference[j] - lowestDifference[j + 1]) <= k):
                        return True
            return False
        
                      
        else:
            return False


"""
This answer is over engineered. runs in 35ms and in one of the bottom solutions.
made countless mistakes and took 2 hours to implement code.
filtered = {k: v for k, v in map1.items() if v > 1}

this line was taken from chatgpt. i was using filter function, but it can give us only keys to store
in new iterable.
Then i starded using 

for key, map1Value in enumerate(filtered):

this line gives you wrong result. here in map1Value i wanted frequency of given key.
But enumerate gives you index and value. To achieve desired key value pair you have to use 

for key, map1Value in filtered.items():

this filtered.items() is an important function in case of dictionaries.


----------------------------------------------------------------------------------------

Following is a simple solution:

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1 : k+i+1]:
                return True
        return False

Just check if current integer again exist in the range upto the distance of k.

"""