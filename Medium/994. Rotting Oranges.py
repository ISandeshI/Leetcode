# 994. Rotting Oranges
# Graph Included
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        visited = [[False] * colLength for _ in range(rowLength)]
        self.maxTime = freshCount = 0
        queue = deque()

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
                if grid[i][j] == 1:
                    freshCount += 1
                    # storing coordinates of all rotten oranges at once, so at a time we can start proceedings.

        while queue and freshCount:
            n = len(queue)
            for k in range(n):
                tup = queue.popleft()
                curRow = tup[0]
                curCol = tup[1]

                if ((curRow - 1) > -1) and grid[curRow - 1][curCol] != 0 and not visited[curRow - 1][curCol]:
                    queue.append((curRow - 1, curCol)) #up
                    visited[curRow - 1][curCol] = True
                    freshCount -= 1

                if ((curCol + 1) < colLength) and grid[curRow][curCol + 1] != 0 and not visited[curRow][curCol + 1]:
                    queue.append((curRow, curCol + 1)) #right
                    visited[curRow][curCol + 1] = True
                    freshCount -= 1

                if ((curRow + 1) < rowLength) and grid[curRow + 1][curCol] != 0 and not visited[curRow + 1][curCol]:
                    queue.append((curRow + 1, curCol)) #down
                    visited[curRow + 1][curCol] = True
                    freshCount -= 1

                if ((curCol - 1) > -1)  and grid[curRow][curCol - 1] != 0 and not visited[curRow][curCol - 1]:
                    queue.append((curRow, curCol - 1)) #left
                    visited[curRow][curCol - 1] = True
                    freshCount -= 1

            self.maxTime += 1

        return -1 if freshCount else self.maxTime
    

"""
Runtime is 0ms and in memory beating only 42% + solutions.
I don't know how this happened. Initialy i thought this is exactly like flood fill or island counting.
But i was so much wrong. So finaly i saw AI's answer. So i followed in with it's logic.
In graph till to the date i come to know about a pattern. If it is not about finding cycle in graph 
then use bfs. it saves us time. DFS goes to find unnecessary paths whereas BFS will find parallely the answer 
and once it get's that we finish the program.
So, use BFS.
"""