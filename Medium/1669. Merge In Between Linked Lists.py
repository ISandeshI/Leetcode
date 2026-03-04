# 1669. Merge In Between Linked Lists
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:


# Build the result list and return its head.

 

# Example 1:


# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
# Example 2:


# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.
 

# Constraints:

# 3 <= list1.length <= 104
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 104

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 1
        temp = ListNode(0, list1)

        while count < a:
            list1 = list1.next
            count += 1

        current = list1.next
        steps = b - a
        while steps > 0:
            current = current.next
            steps -= 1
        
        list1.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = current.next

        return temp.next


"""
i think i am doing a lot overcomplicated solutions. This has runtime of 176ms and beating 81% + solutions 
and in memory beating only 30% + solutions.
Although problem is simple and i can explain but others have smaller solutions.
"""
        
