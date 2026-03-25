# Next Greater Element in Circular Array
# stack included
# Difficulty: MediumAccuracy: 56.97%Submissions: 70K+Points: 4
# Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

# The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

# Note: Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.

# Examples: 

# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation:
# The next greater element for 1 is 3.
# The next greater element for 3 is 4.
# The next greater element for 2 is 4.
# The next greater element for 4 does not exist, so return -1.
# Input: arr[] = [0, 2, 3, 1, 1]
# Output: [2, 3, -1, 2, 2]
# Explanation:
# The next greater element for 0 is 2.
# The next greater element for 2 is 3.
# The next greater element for 3 does not exist, so return -1.
# The next greater element for 1 is 2 (from circular traversal).
# The next greater element for 1 is 2 (from circular traversal).
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 106

class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            curr = arr[i % n]

            while stack and curr >= stack[-1]:
                stack.pop()
                
            if stack and i < n:
                ans[i] = stack[-1]

            stack.append(curr)

        return ans
    

"""
Already solved this in LEETCODE 503, Same code is copied over here.
"""