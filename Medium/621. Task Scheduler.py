# 621. Task Scheduler
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        hashMap = Counter(tasks)
        maxHeap = [-count for count in hashMap.values()] #no need to store which alphabet it is
        # added minus so maximum could come on top because heapq don't have max heap function.
        heapq.heapify(maxHeap)
        queue = deque() #it will store -count and time till it has to be idle

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                # max values are already in negative so adding 1 is like decreasing their value

                if count:
                    queue.append((count, time + n))

            if queue and queue[0][1] <= time:
                tup = queue.popleft()
                heapq.heappush(maxHeap, tup[0])

        return time
    

"""
Runtime is 163ms beating only 41% + solutions and in memory beating only 42% + solutions.
Used all code and logic from Neetcode guy. For more details watch:
https://www.youtube.com/watch?v=s8p8ukTyA2I
"""