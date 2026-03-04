# 1721. Swapping Nodes in a Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        count = 1

        while count < k:
            head = head.next
            count += 1

        kFromStart = head
        kFromEnd = temp.next

        while head.next:
            head = head.next
            kFromEnd = kFromEnd.next
        
        kFromStart.val, kFromEnd.val = kFromEnd.val, kFromStart.val

        return temp.next
    

"""
Again i am telling you my codes are not that good, better solutions are out there.
This code has runtime of 55ms and beating 64% + solutions only and in memory beating only 69% + solutions.
Core logic:
Move pointer first to k-th node from start.
Keep that node stored as kth_from_start.
Now start another pointer second from head.
Move both first and second together until first reaches end.
Now second will be k-th node from end.
Swap values of kth_from_start and second.

"""
        