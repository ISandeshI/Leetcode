# 74. Search a 2D Matrix
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        leftRow = 0
        rightRow = m - 1
        ValidRow = -1
        while leftRow <= rightRow:
            midRow  = (leftRow + rightRow) // 2

            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                ValidRow = midRow
                break

            if matrix[midRow][-1] < target:
                leftRow = midRow + 1

            elif target < matrix[midRow][0]:
                rightRow = midRow - 1

        if ValidRow == -1:
            return False
        
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[ValidRow][mid] == target:
                return True
            
            if target > matrix[ValidRow][mid]:
                low = mid + 1

            else:
                high = mid - 1

        return False
        

"""
This run in 0ms but it beats only 25% in memory.
Solved this in one attempt without any error.
"""
