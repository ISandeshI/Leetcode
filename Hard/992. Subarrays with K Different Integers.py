# 992. Subarrays with K Different Integers
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums, k):
            count = 0
            counter = {}
            left = 0

            for right in range(len(nums)):
                counter[nums[right]] = counter.get(nums[right], 0) + 1
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1

                count += (right - left + 1)

            return count

        return atmost(nums, k) - atmost(nums, k - 1)
    
"""
runtime 125 ms and yet beating 77% + solutions and in memory beating only 24% + solutions.
you won't believe i solved this on mobile, indentation part was hard on mobile so i submited this with knowing 
about error and later adjusted indentation on laptop, surprised to see it run on first time.
This peice of turd just got upgraded with silver coating.
"""

