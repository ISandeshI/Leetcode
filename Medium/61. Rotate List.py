# 61. Rotate List
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        totalLenght = 1
        while current.next:
            current = current.next
            totalLenght += 1

        k = k % totalLenght
        if k == 0:
            return head
        count = 0
        current = head
        tail = None
        while current.next:
            current = current.next
            count += 1
            if count == k:
                tail = head
            elif count > k:
                tail = tail.next
            
        current.next = head
        #circular list is created

    
        head = tail.next
        tail.next = None

        return head
    

"""
runtime is 0ms and beating 88% + solutions in memory.
Took me 2 + hours to figure out the solution. Actual problem was when k is more than length of linked list.
Then i got some errors to handle edge cases. Following lines were added to compensate it:
1. if linked list is blank [] then code gives error, so this is handled by following:
        if not head:
            return None

2. if k = 0, even after updation, then there's no point in running code, we just have keep 
original linked list. So it was handled by following:

        k = k % totalLenght
        if k == 0:
            return head

"""




