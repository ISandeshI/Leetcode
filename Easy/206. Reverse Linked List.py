# 206. Reverse Linked List
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []

        while temp:
            stack.append(temp.val)
            temp = temp.next

        dummy = ListNode()
        dummy.next = head

        while head:
            head.val = stack.pop()
            head = head.next

        return dummy.next
    

"""
Above stacking code runs in 0ms. Following is recursive approach.:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if not head or head.next == None:
                return head
            
            newHead = reverse(head.next)
            front =  head.next
            front.next = head
            head.next = None
            return newHead
        
        return reverse(head)
"""

