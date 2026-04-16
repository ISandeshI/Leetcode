# 222. Count Complete Tree Nodes
# Tree Included
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkLeftHeight(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def checkRightHeight(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.checkLeftHeight(root.left)
        r = self.checkRightHeight(root.right)

        if l == r:
            return ((2**(l + 1)) - 1)
        
        # in a perfect BT, total nodes count is (2^n - 1). That's the formula
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
"""
Runtime is 0ms and in memory beating 88% + solutions.
I just copied the exact code from GFG (Count Number of Nodes in a Binary Tree). 
Solved same over there for both.
In O(n) and above code is more efficient, it is O((log2 n)^2) TC.

"""