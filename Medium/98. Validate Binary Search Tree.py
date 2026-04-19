# 98. Validate Binary Search Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        array = []

        def backtracking(node):
            if self.ans:
                if not node:
                    return
                backtracking(node.left)
                if array and array[-1] >= node.val:
                    self.ans = False
                    return
                else:
                    array.append(node.val)
                backtracking(node.right)

            else:
                return

        backtracking(root)
        return self.ans
    
"""
Runtime is 0ms and in memory beating  79% + solutions.
I used different approach here, traveled inorder fashion, in the meantime if i found non sorted item 
means it is not valid BST.
Following is an alternative approach:

        def backtracking(node, min, max):
            if not node:
                return True
            
            if node.val <= min or node.val >= max:
                return False
            
            leftResult = backtracking(node.left, min, node.val)
            rightResult = backtracking(node.right, node.val, max)

            return leftResult and rightResult

        return backtracking(root, float('-inf'), float('inf'))

"""