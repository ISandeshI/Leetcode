# 88. Merge Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i, j = 0, 0
        merged = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1

            else:
                merged.append(nums2[j])
                j += 1

        if i == m:
            for x in range(j,n):
                merged.append(nums2[x])

        else:
            for x in range(i,m):
                merged.append(nums1[x])
         
        nums1[:] = merged[:]
         
  """
  this question seems simple but this solution is not perfect in terms of space complexity.
  Althugh this answer is number 1 solution with 0ms runtime.

  If you consider space complexity, this solution uses O(m+n) extra space for the merged array.

  best solution available is:

  class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

in this solution we are filling nums1 from the back, so we don't need extra space.
Approach is unique to start from the end of both arrays and fill nums1 from the back.
this is the answer required by MAANG company interview.

  """        
        
        
        
        
        
        
        
        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        