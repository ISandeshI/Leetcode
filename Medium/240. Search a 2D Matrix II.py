# 240. Search a 2D Matrix II
# Medium
# Topics
# premium lock icon
# Companies
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = 0, len(matrix[0]) - 1

        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                return True
            else:
                if target < matrix[row][column]:
                    column -= 1
                else:
                    row += 1

        return False


"""
This became laughing stock, above solution is 151ms of runtime.
I made following changes and yet runtime is still 142ms and beats only 58% solutions.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = 0, len(matrix[0]) - 1

        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                return True
            if target < matrix[row][column]:
                    column -= 1
            if target > matrix[row][column]:
                    row += 1

        return False

All other with lower runtime has similar code.
"""