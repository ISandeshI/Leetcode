# 863. All Nodes Distance K in Binary Tree
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentHashMap = {root: None}
        queue = deque()
        ans = []
        visited = set()
        currDistance = 0

        def dfs(node):
            if not node:
                return
            if node.left:
                parentHashMap[node.left] = node
            if node.right:
                parentHashMap[node.right] = node
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        queue.append(target)
        while queue:
            n = len(queue)
            if currDistance == k:
                for i in range(n):
                    node = queue.popleft()
                    ans.append(node.val)
                break

            for i in range(n):
                currNode = queue.popleft()
                visited.add(currNode)

                if currNode.left and currNode.left not in visited:
                    queue.append(currNode.left)
                if currNode.right and currNode.right not in visited:
                    queue.append(currNode.right)
                if parentHashMap[currNode] and parentHashMap[currNode] not in visited:
                    queue.append(parentHashMap[currNode])
            currDistance += 1

        return ans
    
"""
Runtime is 51ms beating 43% + solutions and in memory beating 39% + solutions.
I solved burning tree GFG problem today, so i knew what will be approach.
So i solved this.
"""