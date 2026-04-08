# Preorder Traversal
# Tree Included
# Difficulty: BasicAccuracy: 62.73%Submissions: 202K+Points: 1Average Time: 15m
# Given the root of a binary tree, your task is to return its Preorder traversal.

# Note: A preorder traversal first visits the node, then visits the left child (including its entire subtree), and finally visits the right child (including its entire subtree).

# Examples:

# Input: root = [1, 4, N, 4, 2]
   
# Output: [1, 4, 4, 2]
# Explanation: The preorder traversal of the given binary tree is [1, 4, 4, 2]
# Input: root = [6, 3, 2, N, 1, 2, N]
    
# Output: [6, 3, 1, 2, 2] 
# Explanation: The preorder traversal of the given binary tree is [6, 3, 1, 2, 2] 
# Constraints:
# 1 ≤ number of nodes ≤ 3*104
# 0 ≤ node->data ≤ 105

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        ans = []

        def backtrack(node):
            if not node:
                return
            
            ans.append(node.data)
            backtrack(node.left)
            backtrack(node.right)

        backtrack(root)
        return ans