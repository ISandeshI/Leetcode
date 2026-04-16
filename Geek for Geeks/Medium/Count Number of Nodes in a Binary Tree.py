# Count Number of Nodes in a Binary Tree
# Tree Included
# Difficulty: MediumAccuracy: 71.6%Submissions: 14K+Points: 4Average Time: 20m
# You are given the root of a complete binary tree. Your task is to find the count of nodes.

# A complete binary tree is a binary tree whose, all levels except the last one are completely filled, the last level may or may not be completely filled and Nodes in the last level are as left as possible.

# Design an algorithm that runs better than O(n).

# Example:

# Input: 
# root = [1,2,3,4,5,6]
# Output: 
# 6
# Explanation: 
# There are a total of 6 nodes in the given tree.
# Your Task:

# Complete the function int cnt_nodes(Node *root), which takes the pointer of the root of the given Binary tree and returns the count of its number of nodes.

# Expected Time Complexity: O((LogN)2).

# Expected Auxiliary Space: O(Log N).

# Constraints:

# 0 <= N (number of nodes) <= 5 * 104 

# 0 <= value of nodes <= 5 * 104

# The tree is guaranteed to be complete.

#User function Template for python3

'''
# Node Class:
class Node:
    def init(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

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
    
    def countNodes(self, root):
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
Above solution is more efficient it has TC of O(log2 n)^2
it just take left height and right height, if same then it will use formula to compute result.
that's why it saves timne. in complete BT, leaf nodes are always filled from left to right side.

while following has TC of O(n)
"""

class Solution:
    def countNodes(self, root):
        self.count = 0
        def backtracking(node):
            if not node:
                return
            
            self.count += 1
            backtracking(node.left)
            backtracking(node.right)

        backtracking(root)
        return self.count