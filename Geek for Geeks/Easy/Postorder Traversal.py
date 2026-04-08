# Postorder Traversal
# Tree Included
# Difficulty: EasyAccuracy: 74.96%Submissions: 151K+Points: 2Average Time: 15m
# Given the root of a Binary Tree, your task is to return its Postorder Traversal.

# Note: A postorder traversal first visits the left child (including its entire subtree), then visits the right child (including its entire subtree), and finally visits the node itself.

# Examples:

# Input: root = [19, 10, 8, 11, 13]

# Output: [11, 13, 10, 8, 19]
# Explanation: The postorder traversal of the given binary tree is [11, 13, 10, 8, 19].
# Input: root = [11, 15, N, 7]
 
# Output: [7, 15, 11]
# Explanation: The postorder traversal of the given binary tree is [7, 15, 11].
# Constraints:
# 1 ≤ number of nodes ≤ 3*104
# 0 ≤ node->data ≤ 105

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        ans = []

        def backtrack(node):
            if not node:
                return
            
            backtrack(node.left)
            backtrack(node.right)
            ans.append(node.data)

        backtrack(root)
        return ans