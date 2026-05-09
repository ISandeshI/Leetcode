# 733. Flood Fill
# Graph Included
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

 

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation:



# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

# Output: [[0,0,0],[0,0,0]]

# Explanation:

# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n


from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        rowLenght = len(image)
        colLenght = len(image[0])
        queue = deque()
        queue.append((sr, sc)) #creating a tuple of currnt row and column

        while queue:
            tup = queue.popleft()
            curRow = tup[0]
            curCol = tup[1]
            if (curRow < 0 or curRow > (rowLenght - 1)) or (curCol < 0 or curCol > (colLenght - 1)) \
            or (image[curRow][curCol] != originalColor) or (image[curRow][curCol] == color):
                continue

            image[curRow][curCol] = color

            if ((curRow - 1) > -1):
                queue.append((curRow - 1, curCol)) #up
            if ((curCol + 1) < colLenght):
                queue.append((curRow, curCol + 1)) #right
            if ((curRow + 1) < rowLenght):
                queue.append((curRow + 1, curCol)) #down
            if ((curCol - 1) > -1):
                queue.append((curRow, curCol - 1)) #left

        return image
    
"""
Runtime for BFS if 0ms and in memory beating 84% + solutions.
I solved this using both, BFS and DFS.
These code look smaller but it requires a lot of thinking.

Runtime of dfs is 0ms and in memory beating only 17% + solutions.
dfs code is so much self explainatory, so no need to explain this

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        rowLenght = len(image)
        colLenght = len(image[0])

        def dfs(curRow, curCol):
            if (curRow < 0 or curRow > (rowLenght - 1)) or (curCol < 0 or curCol > (colLenght - 1)) \
            or (image[curRow][curCol] != originalColor) or (image[curRow][curCol] == color):
                return
            
            # "\"" is used to keep continue coding line on same screen, instead of scrolling long horizontaly
            
            image[curRow][curCol] = color

            dfs(curRow - 1, curCol) #up
            dfs(curRow, curCol + 1) #right
            dfs(curRow + 1, curCol) #down
            dfs(curRow, curCol - 1) #left

        dfs(sr, sc)
        return image
"""