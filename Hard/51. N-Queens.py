# 51. N-Queens
# recursion included
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." ] * n for _ in range(n)]
        col = set() #to store used column
        negDiagonal = set() #to store used cells with (r - c)
        posDiagonal = set() #to store used cells with (r + c)
        ans = []

        def recursion(currentRow):
            if currentRow == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for currentColumn in range(n):
                if currentColumn in col or (currentRow - currentColumn) in negDiagonal or (currentRow + currentColumn) in posDiagonal:
                    continue

                col.add(currentColumn)
                board[currentRow][currentColumn] = "Q"
                negDiagonal.add(currentRow - currentColumn)
                posDiagonal.add(currentRow + currentColumn)

                recursion(currentRow + 1)

                col.remove(currentColumn)
                board[currentRow][currentColumn] = "."
                negDiagonal.remove(currentRow - currentColumn)
                posDiagonal.remove(currentRow + currentColumn)


        recursion(0)
        return ans

"""
runtime 7ms beating 96% + solutions and in memory beating 59% + solutoins.
i didn't do a shit here. Neetcode guy explained this solution very great.
Before solving this we need to understand:
        negDiagonal to store used cells with (r - c)
        posDiagonal to store used cells with (r + c)

this makes this problem very easy to backtrack. There are some coding challenges like:
1. converting n*n 2D matrix to string format like above.

2. creting matrix board
initialy  i wrote: board = [["." * n] for _ in range(n)]
which is: [['...'], ['...'], ['...']]
which is wrong.

then i have to correct it to:
board = [["." ]* 3 for _ in range(3)] 
which is: [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

3. Understanding of removing all element from board and all 3 sets after recursion. And not to return anything
except for base case.

watch this for better understanding:
https://www.youtube.com/watch?v=Ph95IHmRp5M
"""