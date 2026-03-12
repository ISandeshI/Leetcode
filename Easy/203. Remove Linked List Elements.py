# 203. Remove Linked List Elements
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prevNode = temp

        while head:
            if head.val != val:
                prevNode.next = head
                prevNode = prevNode.next
                
            head = head.next
            prevNode.next = None
        return temp.next
    
"""
Never refer this, it is most inefficient answer ever. Runtime 7ms beating 7% + solutions only and in 
memory beating 99% + solutions.

Following was best to understand and has 0ms runtime:

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next


---------------------------------------------------------------------

Following is recursive way. runtime 3ms and beating only 45% + Solutions and in memory beating only 5% +
solutions.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def recursive (Node1):
            if not Node1:
                return None
            
            frontNode = recursive(Node1.next)
            if Node1.val == val:
                return frontNode
            Node1.next = frontNode
            return Node1
    
        return recursive(head)
"""
