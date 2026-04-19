# 235. Lowest Common Ancestor of a Binary Search Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
# according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

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
        self.pFound = False
        self.qFound = False

        def backtracking(node, currArray):
            if not node:
                return
            currArray.append(node)
            if not self.pFound and  node == p:
                self.pFound = True
                self.pList = currArray[:]
                # copying it's values, otherwise it will copy reference, could have used .copy() function also

            if not self.qFound and node == q:
                self.qFound = True
                self.qList = currArray[:]

            if not self.pFound and p.val < node.val:
                backtracking(node.left, currArray)
            if not self.pFound and p.val > node.val:
                backtracking(node.right, currArray)

            if not self.qFound and q.val < node.val:
                backtracking(node.left, currArray)
            if not self.qFound and q.val > node.val:
                backtracking(node.right, currArray)

            currArray.pop()
                     
        backtracking(root, [])

        index = min(len(self.pList), len(self.qList))
        for i in range(index - 1, -1, -1):
            if self.pList[i] == self.qList[i]:
                return self.pList[i]        
            

"""
Runtime is 60ms beating 81% + solutions and in memory beating 84% + solutions.
i modified my existing code from Leetcode 236, We already know due BST where is p and q going to be.
So searching becomes faster.
But also there was no need for this drama.
Basic logic is if 
1. p and q are different side of current node means current node is LCA.
2. if current node is either p or q means that is also our LCA.
3.but if both nodes are in same direction means we haven't yet found our LCA.
For more explaination watch:
https://www.youtube.com/watch?v=TytL24jNZ6k

most simplest and faster code(runtime 58ms beating 88% and in memory beating 98% + solutions):

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root #we are sending back null or answer whatever it is
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

"""