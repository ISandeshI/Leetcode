# 1373. Maximum Sum BST in Binary Tree
# Tree Included
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:



# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
# Example 2:



# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with 
# key equal to 2.
# Example 3:

# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 4 * 104].
# -4 * 104 <= Node.val <= 4 * 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0

        def backtracking(node):
            if not node:
                return(float("inf"), float("-inf"), 0)
            # designed this way, so any leaf node will always be greater than this max and lesser than this min
            # creating a tuple (min, max, sun)

            # now traverse postorder way to later check if current node is root for left and right side in BST
            leftSide = backtracking(node.left)
            rightSide = backtracking(node.right)

            if node.val > leftSide[1] and node.val < rightSide[0]:
                currMin = min(leftSide[0], node.val)
                currMax = max(rightSide[1], node.val)
                currSum = node.val + leftSide[2] + rightSide[2]
                self.maxSum = max(self.maxSum, currSum)
                return (currMin, currMax, currSum)

            else:
                return (float("-inf"), float("inf"), 0)
            # indicating no next parent node can match condition and also no point in telling further about
            # maxSum found till the time, because it is already recorded.


        backtracking(root)
        return self.maxSum


"""
Runtime is 120ms beating only 35% + solutions in memory beating only 88% + solutions.
This code looks very small, but thinking behind this is very time consuming. That's why it is in 
hard category. To know how this is solved or what's logic behind this, watch following explaination 
by Shashcode:
https://www.youtube.com/watch?v=zAz-WbqIaf8

"""