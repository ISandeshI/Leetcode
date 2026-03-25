# 37. Sudoku Solver
# recursion included
# DP included
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Pre-fill sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(currentRow, currentColumn):
            if currentRow == 9:
                return True
            
            if currentColumn == 9:
                return backtrack(currentRow + 1, 0)

            if board[currentRow][currentColumn] != ".":
                return backtrack(currentRow, currentColumn + 1)

            box_index = (currentRow // 3) * 3 + (currentColumn // 3)

            for char in range(1, 10):
                num = str(char)
                if num not in rows[currentRow] and num not in cols[currentColumn] and num not in boxes[box_index]:
                    
                    board[currentRow][currentColumn] = num
                    rows[currentRow].add(num)
                    cols[currentColumn].add(num)
                    boxes[box_index].add(num)

                    if backtrack(currentRow, currentColumn + 1):
                        return True

                    # backtrack
                    board[currentRow][currentColumn] = "."
                    rows[currentRow].remove(num)
                    cols[currentColumn].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0, 0)

"""
Runtime 2051ms Beating 43.36% + solutions and in memory beaing 74.86% + solutions.
Even with the help of AI this solution is not that great.

Tried folowing code using apne ka sapna college, then it got TLE after 6/8. So finaly used AI for memoisation.
because isItSafeToPlace() is taking to much time increasing complexity.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isItSafeToPlace(row, col, digit):
            for j in range(9):
                if board[row][j] == digit:
                    return False
                # check in current row

            for i in range(9):
                if board[i][col] == digit:
                    return False
                # check in current column

            gridRowStart = (row // 3) * 3
            gridColumnStart = (col // 3) * 3

            for k in range(gridRowStart, gridRowStart + 3):
                for l in range(gridColumnStart, gridColumnStart + 3):
                    if board[k][l] == digit:
                        return False
                    
            return True
        

        def backtrack(currentRow, currentColumn):
            if currentRow == 9:
                return True
            
            if currentColumn == 9:
                return backtrack(currentRow + 1, 0)

            if board[currentRow][currentColumn] != ".":
                return backtrack(currentRow, currentColumn + 1)

            for char in range(1, 10):
                if isItSafeToPlace(currentRow, currentColumn, str(char)):
                    board[currentRow][currentColumn] = str(char)
                    if backtrack(currentRow, currentColumn + 1):
                        return True
                    board[currentRow][currentColumn] = "."
            
            return False


        backtrack(0, 0)

"""