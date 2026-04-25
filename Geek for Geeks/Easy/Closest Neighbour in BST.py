# Closest Neighbour in BST
# Tree Included
# Difficulty: EasyAccuracy: 36.98%Submissions: 233K+Points: 2
# Given the root of a binary search tree and a number k, find the greatest number in the binary search tree that is less than or equal to k.

# Note: "If no such node value exists that is smaller than k, then return -1."

# Examples:

# Input: root = [10, 7, 15, 2, 8, 11, 16], k = 14

# Output: 11
# Explanation: The greatest element in the tree which is less than or equal to 14, is 11.
# Input: root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25], k = 24

# Output: 21
# Explanation: The greatest element in the tree which is less than or equal to 24, is 21. 
# Input: root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25], k = 4

# Output: 3
# Explanation: The greatest element in the tree which is less than or equal to 4, is 3.
# Constraints:
# 1 <= number of nodes <= 105
# 1 <= node->data, k <= 105
# All nodes are unique in the BST

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        self.floor = float("-inf")

        def backtracking(node):
            if not node:
                return
            if node.data == k:
                self.floor = k
                return
            
            if node.data > self.floor and node.data < k:
                self.floor = node.data
            if k < node.data:
                backtracking(node.left)
            else:
                backtracking(node.right)

        backtracking(root)
        return -1 if self.floor == float("-inf") else self.floor
    
"""
Tther's another code Ceil in BST in medium section.
Just opposite of current logic. I copied exact code and changed the conditions.
"""