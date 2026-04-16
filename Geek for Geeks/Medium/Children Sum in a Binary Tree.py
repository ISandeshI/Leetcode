# Children Sum in a Binary Tree
# Tree Inlcuded
# Difficulty: MediumAccuracy: 51.58%Submissions: 239K+Points: 4Average Time: 20m
# Given the root of a binary tree, determine whether the tree satisfies the Children Sum Property. In this property, each non-leaf node must have a value equal to the sum of its left and right children's values. A NULL child is considered to have a value of 0, and all leaf nodes are considered valid by default.
# Return true if every node in the tree satisfies this condition, otherwise return false.

# Examples:

# Input: root = [35, 20, 15, 15, 5, 10, 5]

# Output: True
# Explanation: Here, every node is sum of its left and right child.
# Input: root = [1, 4, 3, 5]
  
# Output: False
# Explanation: Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.
# Constraints:
# 1 ≤ number of nodes ≤ 105
# 0 ≤ node->data ≤ 105

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        def backtracking(node):
            if not node:
                return True
            
            if not node.left and not node.right:
                return True

            l = 0 if not node.left else node.left.data
            r = 0 if not node.right else node.right.data
            
            if node.data != l + r:
                return False
            
            return backtracking(node.left) and backtracking(node.right)
        
        return backtracking(root)
