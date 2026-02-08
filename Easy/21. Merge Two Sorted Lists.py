# 21. Merge Two Sorted Lists
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together 
# the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        list3 = temp

        while list1 and list2:

            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
                
            else:
                list3.next = list2
                list2 = list2.next

            list3 = list3.next

        if list1:
            list3.next = list1
        else:
            list3.next = list2

        return temp.next
    
"""
I am officially a turd. Today i take 6 problems and for all i did check with AI.
Obviously this runs in 0ms.

I was not able to know how to keep track of head of list3. With chatgpt i come to know we can create 
a blank node whose next is start of list3.
In the end again we have to check if any list is still in existance (and it will at least one element
from either of the list), then append that all to list3.

"""