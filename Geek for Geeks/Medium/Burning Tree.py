# Burning Tree
# Tree Included
# Difficulty: HardAccuracy: 53.53%Submissions: 144K+Points: 8
# Given the root of a binary tree and a target node, determine the minimum time required to burn the entire tree if the target node is set on fire. In one second, the fire spreads from a node to its left child, right child, and parent.

# Note: The tree contains unique values.

# Examples : 

# Input: root = [1, 2, 3, 4, 5, 6, 7], target = 2
  
# Output: 3
# Explanation: Initially 2 is set to fire at 0 sec 
# At 1 sec: Nodes 4, 5, 1 catches fire.
# At 2 sec: Node 3 catches fire.
# At 3 sec: Nodes 6, 7 catches fire.
# It takes 3s to burn the complete tree.
# Input: root = [1, 2, 3, 4, 5, N, 7, 8, N, N, 10], target = 10

# Output: 5
# Explanation: Initially 10 is set to fire at 0 sec 
# At 1 sec: Node 5 catches fire.
# At 2 sec: Node 2 catches fire.
# At 3 sec: Nodes 1 and 4 catches fire.
# At 4 sec: Node 3 and 8 catches fire.
# At 5 sec: Node 7 catches fire.
# It takes 5s to burn the complete tree.
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
    def minTime(self, root, target):
        parent = {root: None}
        self.targetNode = None
        queue = deque()
        visited = set()
        maxLevel = 0

        def dfs(node):
            if not node:
                return
            
            if node.data == target:
                self.targetNode = node
            
            if node.left:
                parent[node.left] = node
            
            if node.right:
                parent[node.right] = node
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        # now we have dictionary of all nodes and their parents 
        # also we have detected target node from where burning is going to start

        currLevel = 0
        queue.append((self.targetNode, currLevel))

        while queue:
            n = len(queue)
            for _ in range(n):
                tup = queue.popleft()
                # 0th index=node, 1st index = level of bfs

                currNode = tup[0]
                currLevel = tup[1]
                visited.add(currNode)
                maxLevel = max(maxLevel, currLevel)

                if currNode.left and currNode.left not in visited:
                    queue.append((currNode.left, currLevel + 1))
                if currNode.right and currNode.right not in visited:
                    queue.append((currNode.right, currLevel + 1))
                if parent[currNode] and parent[currNode] not in visited:
                    queue.append((parent[currNode], currLevel + 1))

        return maxLevel
    
"""
This was quiet hard problem. There were many components here to keep track of.
I saw following tutor's logic behind this and implemented it. To check the explaination about what is 
happening above, please check the following video. It's quiet big bur worth it:
https://www.youtube.com/watch?v=OOt1jVODA64

"""