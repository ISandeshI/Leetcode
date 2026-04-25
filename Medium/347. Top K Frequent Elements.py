# 347. Top K Frequent Elements
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        arr = []
        for key, val in hashMap.items():
            arr.append((val, key))
        
        arr.sort(reverse = True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans
    
"""
Runtime is 3ms beating 88% + solutions in memory beating 64% + solutions.
This is self explainatory.
Should have solved this using heapq:


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for _, n in heap]
"""