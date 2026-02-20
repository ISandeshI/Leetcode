# 25. Reverse Nodes in k-Group
# Hard
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# --------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseList(subHead):
            if subHead == None or subHead.next == None:
                return subHead
            newHead1 = reverseList(subHead.next)
            front = subHead.next
            front.next = subHead
            subHead.next = None

            return newHead1
        
        def findKthNode(subHead2):
            count = 1
            while count != k and subHead2:
                subHead2 = subHead2.next
                count += 1
            return subHead2

        prevNode = None
        temp = head
        while temp:
            kthNode = findKthNode(temp)
            if prevNode and kthNode == None:
                prevNode.next = temp
                break
            
            nextNode = kthNode.next
            kthNode.next = None
            newHead = reverseList(temp)

            if head == temp:
                head = kthNode #preserve first chunk's updated head

            else:
                prevNode.next = kthNode
            
            prevNode = temp
            temp = nextNode

        return head


            
"""
This code runs in 0ms and beats 37% + solutions in memory. I understood the logic and still couldn't solve 
it. I mean logic is simple you break given linkedlist in sub k length lists, reverse thosse sublists 
and then connect them. Exception for last sublist if it is not with k length.
It took me 3 days to solve and understand this code. I know right after tommorow i will forget how to 
solve it. following is a video, this guy explained each step, although his code is in c++.
There are so many crucial steps involved in this problem and few of edge cased too. That's why 
this is in hard category.
https://www.youtube.com/watch?v=lIar1skcQYI

"""