# 200. Number of Islands
# Graph Included
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        visited = [[False] * colLength for _ in range(rowLength)]
        islandCount = 0

        def dfs(curRow, curCol):
            if (curRow < 0 or curRow > rowLength - 1) or (curCol < 0 or curCol > (colLength - 1)) \
            or (grid[curRow][curCol] == '0') or (visited[curRow][curCol]):
                return

            visited[curRow][curCol] = True

            dfs(curRow - 1, curCol) #up
            dfs(curRow, curCol + 1) #right
            dfs(curRow + 1, curCol) #down
            dfs(curRow, curCol - 1) #left

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    islandCount += 1

        return islandCount




"""
Runtime is 248ms beating only 48% + solutions and in memory beating only 31% + solutions.
This turn outs to be a worst solution. Please do not refer this.

[[False] * colLength for _ in range(rowLength)]
This is the right way to create boolean matrix.

The way we create matrix for integers or strings it is not same for boolean.:

visited = [[False] * colLength] * rowLength

this is wrong. it will create same matrix, but all column values are same reference of forst copy.
so change any cell and all the cells of same columns will get same update.
That's the reason my code was stuck forever. So i made change in line 44.
"""