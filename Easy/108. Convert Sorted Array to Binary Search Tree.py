# 108. Convert Sorted Array to Binary Search Tree
# Tree Included
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createTree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = createTree(left, mid - 1)
            root.right = createTree(mid + 1, right)

            return root
        
        return createTree(0, len(nums) - 1)

    
"""
Runtime is 0ms 0 and in memory beating only 34% + solutions.
I could not solve this simple querry, so used an AI answer.

Initialy itried linked list approach, skewed right and left tree , it becomes bst but not best solution.
Like this:
        3
       / \
      2   4
     /     \
    1       5
   /
  0

"""