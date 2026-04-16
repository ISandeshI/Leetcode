# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create hashmap of inorder data, to find index in future faster
        hashMap = {}
        for ind, val in enumerate(inorder):
            hashMap[val] = ind
        n = m = len(inorder) - 1 # n for preorder and m for inorder last index
        def constructTree(preOrderStartIndex, preOrderEndIndex, inOrderStartIndex, inOrderEndIndex):
            if preOrderStartIndex > preOrderEndIndex or inOrderStartIndex > inOrderEndIndex:
                return None
            rootVal = preorder[preOrderStartIndex]
            rootValIndexInInorder = hashMap[rootVal]
            rootNode = TreeNode(rootVal)
            
            leftTreeSize = rootValIndexInInorder - inOrderStartIndex
            rightTreeSize = inOrderEndIndex - rootValIndexInInorder
            
            rootNode.left = constructTree(preOrderStartIndex + 1, preOrderStartIndex + leftTreeSize, inOrderStartIndex, rootValIndexInInorder - 1)
            rootNode.right = constructTree(preOrderStartIndex + leftTreeSize + 1, preOrderEndIndex, rootValIndexInInorder + 1, inOrderEndIndex)
            
            return rootNode
        
        root = constructTree(0, n, 0, m)
        return root



"""
Runtime id 4ms beating 63% + solutions and in memory beating 56% + solutions.

It is harder to explain what is happening here. So better watch following explaination video:
https://www.youtube.com/watch?v=uDuOuMcSHwo
"""