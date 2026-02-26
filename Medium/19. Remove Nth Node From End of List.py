# 19. Remove Nth Node From End of List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = ListNode()
        temp.next = head

        while head:
            count += 1
            head = head.next

        deleteNode = count - n + 1
        head = temp.next
        count = 0
        prevNode = temp
        while head:
            count += 1
            if count == deleteNode:
                prevNode.next = head.next
                break
            prevNode = head
            head = head.next

        return temp.next


"""
This is one of the worst solution, do not refer it. Runtime is 3ms and beating only 6% + solutions and 
in memory beating only 22% + solutions. Most of the solutions have 0ms runtime.
check the following: there's some big thinking but it is worth

def removeNthFromEnd(self, head, n):

    ans = ListNode(0, head)
    curr = ans

    for i in range(n):
        head = head.next

    while head:
        head = head.next
        curr = curr.next

    curr.next = curr.next.next

    return ans.next

Approach:
1. 
ex. Original: 1 → 2 → 3 → 4 → 5, n = 2
we create duummy named ans before head:

Dummy:   0 → 1 → 2 → 3 → 4 → 5

2. Initialize Slow Pointer curr = ans
it stays back.

3. Move Fast Pointer n Steps ahead, head is fast pointer.
Dummy → 1 → 2 → 3 → 4 → 5
curr
head after loop → 3

now distance between curr and head = n nodes

4.now move both simultaneously until head is at end which is none and
curr will be exactly before the node we want to delete.

Now: curr = 3
and we want to delete 4.

5.
curr.next = curr.next.next
Before:
3 → 4 → 5

After:
3 → 5

6. Return the Real Head
return ans.next

"""