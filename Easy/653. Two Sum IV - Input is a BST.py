# 653. Two Sum IV - Input is a BST
# Tree Included
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        required = []
        self.ans = False
        def backtracking(node):
            if not self.ans:
                if not node:
                    return
                
                if node.val in required:
                    self.ans = True
                    return
                
                requiredInt = k - node.val
                required.append(requiredInt)
                
                backtracking(node.left)
                backtracking(node.right)

            else:
                return        

        backtracking(root)
        return self.ans
    
"""
Runtime is 25ms beating only 6% + solutions and in memory beating 98% + solutions. 
This is one of the worst solution. Array made this slow. When i used set instead runtime became 4ms
beating 61% + solutions.

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        required = set()
        self.ans = False
        def backtracking(node):
            if not self.ans:
                if not node:
                    return
                
                if node.val in required:
                    self.ans = True
                    return
                
                requiredInt = k - node.val
                required.add(requiredInt)
                
                backtracking(node.left)
                backtracking(node.right)

            else:
                return        

        backtracking(root)
        return self.ans


"""