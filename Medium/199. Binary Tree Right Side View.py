# 199. Binary Tree Right Side View
# Tree included
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == (n - 1):
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
    
"""
Runtime is 0ms and in memory beating 94% + solutions.
Due to practise it was realy simple for me.
Core logic is last element on each level is candidate with most right side view.

"""