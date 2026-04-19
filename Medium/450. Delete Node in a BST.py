# 450. Delete Node in a BST
# Tree Included
# Medium
# Topics
# premium lock icon
# Companies
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def preDecessor(node):
            while node.right:
                node = node.right
            return node
        
        def successor(node):
            while node.left:
                node = node.left
            return node

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # match found
            # case1 leaf node
            if not root.left and not root.right:
                return None
        
            # case2 only one child found on right side
            elif not root.left:
                return root.right
            # case3 only one child found on left side
            elif not root.right:
                return root.left
            # case4 both childs are there
            # let's go with inorder predecessor from left tree
            else:
                # preNode = preDecessor(root.left)
                # root.val = preNode.val
                # root.left = self.deleteNode(root.left, preNode.val)
                
                # let's go with inorder successor from right tree
                sucNode = successor(root.right)
                root.val = sucNode.val
                root.right = self.deleteNode(root.right, sucNode.val)

        return root
    

"""
Runtime is 0ms and in memory beating 49% + solutions.
There are two ways to resolve root deletion when it has two children. 1. inorder predecessor
2. inorder successor. i have written both above and you can check either one of them

Used shashcode's logic, you can see his explaination on following:
https://www.youtube.com/watch?v=kdXBGjmiVCE

"""