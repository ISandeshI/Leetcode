# 110. Balanced Binary Tree
# Tree Included
# Easy
# Topics
# premium lock icon
# Companies
# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def backtracking(node):
            if not node:
                return 0
            
            leftHeight = backtracking(node.left)
            if leftHeight == -1:
                return -1
            
            rightHeight = backtracking(node.right)
            if rightHeight == -1:
                return -1
            
            if abs(rightHeight - leftHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)

        return (backtracking(root) != -1)
    

"""
Runtime is 0ms and in memory beating 94% + solutions.
If you solve this on your own, you will find that it is at least medium problem.
used shashcode's logic.

"""