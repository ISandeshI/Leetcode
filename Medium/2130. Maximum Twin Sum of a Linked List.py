# 2130. Maximum Twin Sum of a Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 
# Example 2:


# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
# Example 3:


# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

# Constraints:

# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head1):
            if not head1 or not head1.next:
                return head1
            
            newHead = reverse(head1.next)
            front = head1.next
            front.next = head1
            head1.next = None
            return newHead
        
        temp = ListNode(0, head)

        slowPointer, fastPointer = temp, head
        #here we are not trying to reach one step ahead of half, we need to reach at the end of half
        #example: [1,2] our half is at one, and we need our slowPointer at one. If we wanted to cross it 
        #just after 1, then we would have started both of them from head.

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        head2 = reverse(slowPointer.next)
        slowPointer.next = None
        head1 = temp.next

        maxSum = 0

        while head1 and head2:
            maxSum = max(maxSum, (head1.val + head2.val))
            head1 = head1.next
            head2 = head2.next

        return maxSum

"""
Above solution has runtime of 101ms and beating 11% + soltions and in memory beating 30% + solutions.
This is slow because of recursive calls made in reverse() function. Time complexity is still O(n), 
but recursion adds overhead.

What happens internally:
For n/2 nodes → you create n/2 recursive calls
Each call:
Adds function-call overhead
Uses stack memory
Python recursion is slower than iteration
Python does NOT optimize tail recursion
So while time complexity is still O(n),
constant factor is larger → slower runtime.
-----------------------------------------------------------------------------------------

Following reverse() function was added to same code above and then our 
solution has runtime of 54ms and beating 84% + soltions and in memory beating 60% + solutions:

        def reverse(head1):
            prev = None
            curr = head1
            
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            return prev
"""