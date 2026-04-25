# Ceil in BST
# Tree Included
# Difficulty: MediumAccuracy: 62.73%Submissions: 184K+Points: 4Average Time: 30m
# You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.
# Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
# If Ceil could not be found, return -1.

# Examples:

# Input: root = [5, 1, 7, N, 2, N, N, N, 3], x = 3

# Output: 3
# Explanation: We find 3 in BST, so ceil of 3 is 3.
# Input: root = [10, 5, 11, 4, 7, N, N, N, N, N, 8], x = 6

# Output: 7
# Explanation: We find 7 in BST, so ceil of 6 is 7.
# Constraints:
# 1  ≤ Number of nodes  ≤ 105
# 1  ≤ Value of nodes ≤ 105

''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        self.ceil = float("inf")

        def backtracking(node):
            if not node:
                return
            if node.data == x:
                self.ceil = x
                return
            
            if node.data < self.ceil and node.data > x:
                self.ceil = node.data
            if x < node.data:
                backtracking(node.left)
            else:
                backtracking(node.right)

        backtracking(root)
        return -1 if self.ceil == float("inf") else self.ceil
    
"""
Initialy i wrote self.ceil =  106 after checking conditions.
But after pasting it here power of any digit is vanished.
so it is not 105 it is 10^5 or 10**5
"""