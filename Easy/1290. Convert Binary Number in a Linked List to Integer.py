# 1290. Convert Binary Number in a Linked List to Integer
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

 

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

# ----------------------------------------------------------------------

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        str1 = ""
        while head:
            str1 += head.val
            head = head.next

        return int(str1, base = 2)
    


"""
This code runs in 0ms and beating 76% + solutions in memory. Very easy no need to explain.
Initialy i wrote following on line 44:
str1 += head.val

basicaly string cannot concatenate int type to it. So i have to convert it to string first.
"""