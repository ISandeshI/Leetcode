# 547. Number of Provinces
# Graph included
# Medium
# Topics
# premium lock icon
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        queue = deque()
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True
                
                while queue:
                    city = queue.popleft()
                    for j in range(n):
                        if isConnected[city][j] == 1 and not visited[j]:
                            visited[j] = True
                            queue.append(j)

        return count           

"""
Runtime 4ms beating only 67% + solutions and in memory beating only 89% + solutions.
This is an AI generated answer not mine.

Initialy i thought this is very similar to 200. number of islands, just wording is altered, 
but task remains same.
And i was wrong. we just need plain traversal that's it. if traversal stops check 
if visited is traveled or not.

DFS solution is much simpler:

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(city):
            visited[city] = True

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count


"""