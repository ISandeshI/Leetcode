# 463. Island Perimeter
# Easy
# Topics
# premium lock icon
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4

class Solution:
    def islandPerimeter(self, grid: List[List[int]]):
        rows = len(grid)
        columns = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    if j == 0: #counting leftmost boundries of grid
                        perimeter += 1
                    else:
                        if grid[i][j - 1] == 0: #if inside left is water
                            perimeter += 1
                    
                    if j == (columns - 1): #counting rightmost boundries of grid
                        perimeter += 1
                    else:
                        if grid[i][j + 1] == 0: #if inside right is water
                            perimeter += 1
                    
                    if i == 0: #counting topmost boundries of grid
                        perimeter += 1
                    else:
                        if grid[i - 1][j] == 0: #if inside top is water
                            perimeter += 1
                    
                    if i == (rows - 1): #counting bottom-most boundries of grid
                        perimeter += 1
                    else:
                        if grid[i + 1][j] == 0: #if inside bottom is water
                            perimeter += 1   

        return perimeter

"""
this runs in 34ms and beats 70% + solutions out there.
Following is one of simplest solution:
Key idea

Every land cell (1) starts with 4 sides
Each shared edge between two land cells removes 2 sides (because both cells lose 1)
Because one shared edge removes one side from both cells.

Example (quick)

For two adjacent land cells:

1 1


Each adds +4 = 8
They share one edge → subtract 2
Final = 6 ✅

code:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter
"""