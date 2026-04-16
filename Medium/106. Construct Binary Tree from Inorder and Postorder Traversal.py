# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # create hashmap of inorder data, to find index in future faster
        hashMap = {}
        for ind, val in enumerate(inorder):
            hashMap[val] = ind
        
        n = m = len(inorder) - 1 # n for postorder and m for inorder last index
        
        def constructTree(postOrderStartIndex, postOrderEndIndex, inOrderStartIndex, inOrderEndIndex):
            if postOrderStartIndex > postOrderEndIndex or inOrderStartIndex > inOrderEndIndex:
                return None
            rootVal = postorder[postOrderEndIndex]
            rootValIndexInInorder = hashMap[rootVal]
            rootNode = TreeNode(rootVal)
            
            leftTreeSize = rootValIndexInInorder - inOrderStartIndex
            rightTreeSize = inOrderEndIndex - rootValIndexInInorder
            
            rootNode.left = constructTree(postOrderStartIndex, postOrderStartIndex + leftTreeSize - 1, inOrderStartIndex, rootValIndexInInorder - 1)
            rootNode.right = constructTree(postOrderStartIndex + leftTreeSize, postOrderEndIndex - 1, rootValIndexInInorder + 1, inOrderEndIndex)
            
            return rootNode
        
        root = constructTree(0, n, 0, m)
        return root



"""
Runtime id 3ms beating 73% + solutions and in memory beating 46% + solutions.

Most of the code is copied from 105, made little changes according to problem statement.
It is harder to explain what is happening here. So better watch following explaination video:
https://www.youtube.com/watch?v=uDuOuMcSHwo
"""