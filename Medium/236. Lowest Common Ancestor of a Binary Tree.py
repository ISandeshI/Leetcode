# 236. Lowest Common Ancestor of a Binary Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pList = []
        self.qList = []
        self.foundBoth = 0

        def backtracking(node, currArray):
            if not node:
                return
            currArray.append(node)
            if node == p:
                self.foundBoth += 1
                self.pList = currArray[:]
                # copying it's values, otherwise it will copy reference, could have used .copy() function also

            if node == q:
                self.foundBoth += 1
                self.qList = currArray[:]

            if self.foundBoth < 2:
                backtracking(node.left, currArray)
            if self.foundBoth < 2:
                backtracking(node.right, currArray)
            currArray.pop()
            
            """
            i have to do pop(), because in both recursive functions currArray is passed by Reference
            so whatever values we pass, they go as object referencing same memory and this array keeps
            growing, i tried using copy function to pass it as value but it makes code a lot slower.
            so decided to pop element from array itself"""
            
        backtracking(root, [])
        index = min(len(self.pList), len(self.qList))
        for i in range(index - 1, -1, -1):
            if self.pList[i] == self.qList[i]:
                return self.pList[i]

"""
Runtime is 49ms beating 95% + solutions and in memory beating 59% + solutions.
"""