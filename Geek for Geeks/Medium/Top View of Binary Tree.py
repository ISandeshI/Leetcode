# Top View of Binary Tree
# Tree Included
# Difficulty: MediumAccuracy: 38.43%Submissions: 453K+Points: 4Average Time: 45m
# You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# Note:

# Return the nodes from the leftmost node to the rightmost node.
# If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 
# Examples:

# Input: root = [1, 2, 3]
# Output: [2, 1, 3]
# Explanation: The Green colored nodes represents the top view in the below Binary tree.
 
# Input: root = [10, 20, 30, 40, 60, 90, 100]
# Output: [40, 20, 10, 30, 100]
# Explanation: The Green colored nodes represents the top view in the below Binary tree.


# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node->data ≤ 105

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:
    def topView(self, root):
        ans = []
        hashMap = {}
        
        # custom data type with tuple (node, column index)
        node = (root, 0)
        queue = deque()
        queue.append(node)

        while queue:
            n = len(queue)
            for i in range(n):
                node1 = queue.popleft()
                if node1[1] not in hashMap:
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
To know about what we did here in details, check out shashcode's logic:
https://www.youtube.com/watch?v=zbA4yWuEoYE
"""