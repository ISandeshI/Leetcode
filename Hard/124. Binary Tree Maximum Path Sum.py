# 124. Binary Tree Maximum Path Sum
# Tree Included
# Hard
# Topics
# premium lock icon
# Companies
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        
        def backtracking(node):
            if not node:
                return 0
            
            leftSum = max(0, backtracking(node.left))
            rightSum = max(0, backtracking(node.right))
            # If subtree is negative → don’t take it

            self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)

            return node.val + max(leftSum, rightSum)

        backtracking(root)
        return self.maxSum
    
"""
Runtime is 5ms beating 84% + solutions and in memory beating 67% + solution.
This code looks smaller but thinking is very time consuming.
Previously i had close up code but it started collapsing for edge cases, so i started adding exceptions.
I should have know that this means code is not optimised.
So took help of AI, it told most important thing, do not take negative value from bottom side, instead 
we can ignore it and choose 0. that's why line number 48 - 49 are important.
"""