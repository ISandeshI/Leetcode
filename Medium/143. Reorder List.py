# 143. Reorder List
# Medium
# Topics
# premium lock icon
# Companies
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(Node1):
            if not Node1 or Node1.next is None:
                return Node1
            
            newHead = reverse(Node1.next)
            front = Node1.next
            front.next = Node1
            Node1.next = None
            return newHead         
        
        count = 1
        temp = ListNode(0, head)

        while head:
            head = head.next
            count += 1

        half = (count + 1) // 2
        head = temp.next
        for i in range(1, half + 1):
            if i == half:
                current = head
            head = head.next
        current.next = None

        head2 = reverse(head)
        head = temp.next
        curr = ListNode()
        while head and head2:
            if head2:
                curr = head
                head = head.next
                curr.next = head2
            if head:
                curr = head2
                head2 = head2.next
                curr.next = head

        head = temp.next

"""
Do not refere this, it is worst solution has runtime 7ms beating 18% + solutions and in memory beating only 
6% + solutions.
A lot of things are done manualy so making code slow.
1. while dividing list in half, use fast and slow pointer technique.
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# slow is now at middle

2. for swapping one's pointer to another alternately use following code:

first = head
second = head2
        
while second:
    tmp1 = first.next
    tmp2 = second.next
    
    first.next = second
    second.next = tmp1
    
    first = tmp1
    second = tmp2


"""