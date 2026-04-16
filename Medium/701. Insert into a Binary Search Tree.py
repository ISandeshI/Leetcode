# 701. Insert into a Binary Search Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root  = TreeNode(val)
            return root
        
        def backtracking(node):
            if not node:
                node = TreeNode(val)
                return node
            
            if val > node.val:
                if not node.right:
                    node.right = backtracking(node.right)
                else:
                    backtracking(node.right)
            if val < node.val:
                if not node.left:
                    node.left = backtracking(node.left)
                else:
                    backtracking(node.left)

        backtracking(root)
        return root
    
"""
Runtime is 7ms beating only 7% + solutions and in memory beating only 59% + solutions.
This is worst solution. Do not refer it please. You should return node after assigning it to left or right 
this way updated root is sent back.

Following is best solution with 0ms runtime:

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def backtracking(node):
            if not node:
                node1 = TreeNode(val)
                return node1
            
            if val > node.val:
                node.right = backtracking(node.right)
            if val < node.val:
                node.left = backtracking(node.left)
            
            return node

        return backtracking(root)
"""