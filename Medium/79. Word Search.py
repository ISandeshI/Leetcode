# 79. Word Search
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLength = len(board)
        columnLength = len(board[0])

        def recursion(currentRow, currentColumn, wordIndex):
            if wordIndex == len(word):
                return True
            
            if currentRow < 0 or currentRow >= rowLength or currentColumn < 0 or currentColumn >= columnLength:
                return False
            if board[currentRow][currentColumn] == "$" or board[currentRow][currentColumn] != word[wordIndex]:
                return False
            
            char = board[currentRow][currentColumn]
            board[currentRow][currentColumn] = "$"

            if (recursion(currentRow, currentColumn + 1, wordIndex + 1) or \
            recursion(currentRow, currentColumn - 1, wordIndex + 1) or \
            recursion(currentRow + 1, currentColumn, wordIndex + 1) or \
            recursion(currentRow - 1, currentColumn, wordIndex + 1)):
                return True

            board[currentRow][currentColumn] = char
            return False
            
        for row in range(rowLength):
            for col in range(columnLength):
                if board[row][col] == word[0]:
                    ans = recursion(row, col, 0)
                    if ans:
                        return True
                    
        return False
                
"""
Runtime is 3457ms Beating 70.75% + solutions and in Memory beating 50.80% + solutions.
I didn't do anything. Shashcode guy did it. Basicaly it is not only recursion or backtracking.
It involves DFS.
"""