# 23. Merge k Sorted Lists
# Hard
# Topics
# premium lock icon
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
# --------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None #important line for edge case
        
        return self.divideLists(lists, 0, len(lists) - 1)
    
    def divideLists(self, currentList, low, high):
        if low == high:
            return currentList[low] # this is the base case where we return one single list for futher merging
        
        mid = (low + high) // 2

        leftPart = self.divideLists(currentList, low, mid)
        rightPart = self.divideLists(currentList, mid + 1, high)
        #we kept them dividing until we get one single list.
        #then merge them together using following function.
        #now merge this final list with another final list
        #keep this doing until we get only sinlge list which is already sorted

        return self.mergTwoOnly(leftPart, rightPart)
        
    def mergTwoOnly(self, list1, list2):
        temp = ListNode()
        finList = temp

        while list1 and list2:
            if list1.val <= list2.val:
                finList.next = list1
                list1 = list1.next
            else:
                finList.next = list2
                list2 = list2.next

            finList = finList.next

        finList.next = list1 if list1 else list2

        return temp.next
                    

"""
Stolen approach from AI. It runs in 15ms and beats only 31% + solutions.
Don't ever think about getting all values one by one in an array and then sorting it 
and then creating a new list. It has more of time as well as space complexity.
above code is good in terms of complexity. There is another approach of using heap.
But to understand this you will have to follow:
Learning Order Summary:
Lists & indexing
Binary tree (concept only)
Sorting + key
Priority Queue idea
Heap using heapq

-------------------------------------------------------------------
Use a min-heap (priority queue) to always pick the smallest current element among the k lists.
Steps:

Create a min-heap.
Insert the head node of each non-empty list into the heap.

Repeatedly:
Extract the smallest node from the heap.
Add it to the result list.
If the extracted node has a next, push that next node into the heap.

Continue until the heap is empty.
Code:

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        # Push head of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

"""