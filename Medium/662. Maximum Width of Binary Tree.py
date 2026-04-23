# 662. Maximum Width of Binary Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
# Example 2:


# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
# Example 3:


# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = float("-inf")
        queue = deque()
        queue.append((root, 0)) #storing in tuple (node, index) 0th node and 1st as index
        # pushing heap index of each node with unique value. starting from 0
        # left will be (2*i) + 1 and right will be (2*i) + 2

        while queue:
            n = len(queue)
            startIndex = queue[0][1]
            endIndex = queue[-1][1]
            maxWidth = max(maxWidth, endIndex - startIndex + 1)

            for i in range(n):
                tup = queue.popleft()
                node = tup[0]
                id = tup[1]
                
                if node.left:
                    queue.append((node.left, (2 * id) + 1))
                if node.right:
                    queue.append((node.right, (2 * id) + 2))

        return maxWidth


"""
Runtime is 0ms and in memory beating 59% + solutions.
This problem code looks very small but you have to have knowledge about a lot of things.
If you want to know what exactly we did here, please check following Apna college video:
https://www.youtube.com/watch?v=rhz-csskg_A
"""