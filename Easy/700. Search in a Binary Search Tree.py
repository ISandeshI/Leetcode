# 700. Search in a Binary Search Tree
# Tree included
# Easy
# Topics
# premium lock icon
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None
        def backtracking(node):
            if not node:
                return
            
            if node.val == val:
                self.ans = node
                return
            elif node.val > val:
                backtracking(node.left)
            elif node.val < val:
                backtracking(node.right)

        backtracking(root)
        return self.ans
    
"""
Runtime is 3ms beating only 13% +solutions and in memory beating only 16% + solutions.
There was no need to create separate variable, it is causing extra time and space and hence the delay.
Following is best solution with 0ms runtime:

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return

        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)

        return False
"""