# 234. Palindrome Linked List
# recursion included
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

#Let's practise recursion

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(Node):
            if not Node or not Node.next:
                return Node
            
            newHead = reverse(Node.next)
            Node.next.next = Node
            Node.next = None
            return newHead
        
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        head2 = reverse(slowPointer)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True
    

"""
Runtime 74ms and beating only 6% + solutions.
To practise recursion we choose this method.
Following is perfect full recursion for this problem:


class Solution:
    def isPalindrome(self, head):
        self.left = head
        
        def dfs(right):
            if not right:
                return True
            
            if not dfs(right.next):
                return False

            # This line does two things simultaneously:
            # 1. Calls recursion to go deeper in the list.
            # 2. Stops execution early if a mismatch was already found.

            # dfs(right.next)
            # is always executed.
            # The if only checks what the recursive call returned.
            
            if self.left.val != right.val:
                return False
            
            self.left = self.left.next
            return True
        
        return dfs(head)

"""