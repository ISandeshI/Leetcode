# Tree Boundary Traversal
# Tree Included
# Difficulty: MediumAccuracy: 23.33%Submissions: 545K+Points: 4Average Time: 35m
# Given a root of a Binary Tree, return its boundary traversal in the following order:

# Left Boundary: Nodes from the root to the leftmost non-leaf node, preferring the left child over the right and excluding leaves.

# Leaf Nodes: All leaf nodes from left to right, covering every leaf in the tree.

# Reverse Right Boundary: Nodes from the root to the rightmost non-leaf node, preferring the right child over the left, excluding leaves, and added in reverse order.

# Note: The root is included once, leaves are added separately to avoid repetition, and the right boundary follows traversal preference not the path from the rightmost leaf.

# Examples:

# Input: root = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
# Output: [1, 2, 4, 8, 9, 6, 7, 3]
# Explanation:

# Input: root = [1, N, 2, N, 3, N, 4, N, N] 
# Output: [1, 4, 3, 2]
# Explanation:

# Left boundary: [1] (as there is no left subtree)
# Leaf nodes: [4]
# Right boundary: [3, 2] (in reverse order)
# Final traversal: [1, 4, 3, 2]
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

class Solution:
    def boundaryTraversal(self, root):
        leftTravelResult = []
        leafTravel = []
        rightTravelResult = []

        def isLeaf(node):
            if not node.left and not node.right:
                return True
            
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                leafTravel.append(node.data)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        def leftTravel(node):
            node = node.left
            while node:
                if not isLeaf(node):
                    leftTravelResult.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        def rightTravel(node):
            node = node.right
            while node:
                if not isLeaf(node):
                    rightTravelResult.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left


        if not isLeaf(root):
            leftTravelResult.append(root.data)
            
        leftTravel(root)    
        addLeaves(root)
        rightTravel(root)
            
        return leftTravelResult + leafTravel + rightTravelResult[::-1]
    

"""
i tried many ways with my own logic but failed, so i checked out shashcode's algorithm, i was trying 
to find solution in O(n) TC. But it is not possble in any case. 
That's the reason for finding leafs we have to go through each node in tree that increases our TC.
For detailed explaination watch this:
https://www.youtube.com/watch?v=c2uD7WBjE5A

"""