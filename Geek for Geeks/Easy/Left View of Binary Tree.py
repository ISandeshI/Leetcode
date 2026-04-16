# Left View of Binary Tree
# Tree Included
# Difficulty: EasyAccuracy: 33.74%Submissions: 600K+Points: 2Average Time: 20m
# Given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

# Note: If the tree is empty, return an empty list.

# Examples :

# Input: root = [1, 2, 3, 4, 5, N, N]

# Output:[1, 2, 4]
# Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

# Input: root = [1, 2, 3, N, N, 4, N, N, 5, N, N]

# Output: [1, 2, 4, 5]
# Explanation: From the left side of the tree, only the nodes 1, 2, 4, and 5 are visible.

# Constraints:
# 0 ≤ number of nodes ≤ 105
# 0 ≤ node -> data ≤ 105

''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

from collections import deque
class Solution:
    def leftView(self, root):
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                if i == 0:
                    ans.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans