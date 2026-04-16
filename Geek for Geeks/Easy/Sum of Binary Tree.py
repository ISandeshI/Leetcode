# Sum of Binary Tree
# Tree Included
# Difficulty: BasicAccuracy: 77.27%Submissions: 58K+Points: 1
# Given a binary tree, find the sum of values of all the nodes. 

# Examples:

# Input: root = [10, 20, 30, 40, 60, N, N]
#            10
#          /   \
#         20    30
#       /    \
#     40     60
# Output: 160
# Explanation: The sum of all the nodes is 10 + 20 + 30 + 40 + 60.
# Input: root = [1, 3, 2]
#       1
#     /   \
#    3     2
# Output: 6
# Explanation: The sum of all the nodes is 1 + 2 + 3 = 6.
# Input: root = [1, 2, N, 4, N]
#            1
#          /     
#         2    
#       /   
#     4     
# Output: 7
# Explanation: The sum of all the nodes is 1 + 2 + 4 = 7.
# Constraints:
# 1 <= number of nodes <= 104
# -105 <= node->data <= 105

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        self.sum = 0

        def backtracking(node):
            if not node:
                return
            
            self.sum += node.data

            backtracking(node.left)
            backtracking(node.right)

        backtracking(root)
        return self.sum