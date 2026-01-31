# 83. Remove Duplicates from Sorted List
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
-----------------------------------------------------------------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        if head:
            currentNode =  head
            while currentNode.next != None:
                if currentNode.val == currentNode.next.val:
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next

            return head
        
        else:
            return None


    """
    Made a lot of silly mistakes in starting like not checking if head is None.
    if linked list is empty return None (Remember this base case).
                    if currentNode.val == currentNode.next.val:
                        currentNode.next = currentNode.next.next
            
                    currentNode = currentNode.next

    This was my previous line. Here is one mistake.
    Cosider 1->1->1->2
    when currentNode is first 1
    it will check and remove second 1
    then currentNode will move to second 1
    but second 1 is also duplicate so it should not move forward
    so we need to put currentNode = currentNode.next in else block only

    With this updated code we are moving forward only when we are sure that next node is not duplicate.
    And if it is duplicate we are just changing the pointer of current node to next one.                    

    """