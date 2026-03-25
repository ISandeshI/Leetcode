# Next Greater Element
# stack included
# Difficulty: MediumAccuracy: 32.95%Submissions: 512K+Points: 4Average Time: 20m
# You are given an array arr[] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1.

# Examples

# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
# Input: arr[] = [6, 8, 0, 1, 3]
# Output: [8, -1, 1, 3, -1]
# Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1, for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
# Input: arr[] = [1, 2, 3, 5]
# Output: [2, 3, 5, -1]
# Explanation: For a sorted array, the next element is next greater element also except for the last element.
# Input: arr[] = [5, 4, 3, 1]
# Output: [-1, -1, -1, -1]
# Explanation: There is no next greater element for any of the elements in the array, so all are -1.
# Constraints:
# 1 ≤ arr.size() ≤ 106
# 0 ≤ arr[i] ≤ 109

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(arr[i])

        return ans
    
"""
I didn't do anything, someone has realy thought through this problem to solve it in O(n) time.

Approach:

Traverse array from right → left
Use a stack to store potential next greater elements

Steps:

Initialize empty stack
For each element:
Pop all elements ≤ current
If stack not empty → top = answer
Else → -1
Push current element into stack

Key Idea:
Stack always keeps greater elements only
Smaller elements are useless → removed

Why Efficient
Each element is pushed and popped once
→ O(n) time

"""
