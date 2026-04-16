# 559. Maximum Depth of N-ary Tree
# Tree Included
# Easy
# Topics
# premium lock icon
# Companies
# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5
 

# Constraints:

# The total number of nodes is in the range [0, 104].
# The depth of the n-ary tree is less than or equal to 1000.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        self.depth = 0
        
        def backtracking(node, currDepth):
            self.depth = max(self.depth, currDepth)
            if not node.children:
                return
            
            for node1 in node.children:
                backtracking(node1, currDepth + 1)


        backtracking(root, 1)
        return self.depth
    


"""
Runtime 47ms beating 84% + solutions and in memory beating only 35% + solutions.
Used same logic as Leetcode 104, Instead of BT we have to access an array of nodes.

Best and shortest solution with top score of 31ms:

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxVal = 1
        for child in root.children:
            maxVal = max(maxVal, 1 + self.maxDepth(child))
        return maxVal
"""