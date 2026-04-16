# Bottom View of Binary Tree
# Tree Included
# Difficulty: MediumAccuracy: 54.18%Submissions: 350K+Points: 4Average Time: 45m
# You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

# Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.

# Examples :

# Input: root = [1, 2, 3, 4, 5, N, 6]
    
# Output: [4, 2, 5, 3, 6]
# Explanation: The Green nodes represent the bottom view of below binary tree.
    
# Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
    
# Output: [5, 10, 4, 28, 25]
# Explanation: The Green nodes represent the bottom view of below binary tree.
    
# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node->data ≤ 105

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque
class Solution:
    def bottomView(self, root):
        ans = []
        hashMap = {}
        queue = deque()
        node = (root, 0) #making new data type tuple to store node and it's column value
        queue.append(node)

        while queue:
            n = len(queue)
            for i in range(n):
                node1 = queue.popleft()
                hashMap[node1[1]] = node1[0].data

                if node1[0].left:
                    node = (node1[0].left, node1[1] - 1)
                    queue.append(node)
                if node1[0].right:
                    node = (node1[0].right, node1[1] + 1)
                    queue.append(node)
                
        for key in sorted(hashMap):
            ans.append(hashMap[key])

        return ans
    
"""
To know logic behind how it is constructed, check out shashcode's logic:
https://www.youtube.com/watch?v=zbA4yWuEoYE

start watching after 19:34
"""