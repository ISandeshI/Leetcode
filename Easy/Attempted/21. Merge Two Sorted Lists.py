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
        list3 = ListNode()
          
        if list1.val <= list2.val:
                list3 = list1
                list1 = list1.next

        else:
                list3 = list2
                list2 = list2.next
        temp = list3

        while list1.next == None or list2.next == None:

            if list1.val <= list2.val:
                list1 = list1.next
                temp.next = list1

            else:
                list2 = list2.next
                temp.next = list2

            temp = temp.next

        return list3