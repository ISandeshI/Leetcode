# 6. Zigzag Conversion
# Medium
# Topics
# premium lock icon
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        matrix = [""] * numRows
        rowCount = 0
        direction = -1 #for going up
        for char in s:
            if rowCount == 0 or rowCount == numRows - 1:
                direction *= -1

            matrix[rowCount] += char
            rowCount += direction
        
        return "".join(matrix)
            
"""
I couldn't solve this so used chatgpt. This obviously runs in 4ms and among top 95% + solutions.
Initialy i was thinking about actualy building whole matrix and then printing it in the end.
Instead this is great approach.

Simple Approach -->
Step-by-step logic
Edge case
If numRows == 1 → return the string as is
(No zigzag possible)

Create storage
Create numRows empty strings (or lists)
Each represents one row
Track direction

Use:
current_row
direction (down or up)
Iterate over characters
Add each character to rows[current_row]

If at:
top row → change direction to down
bottom row → change direction to up
Move current_row accordingly
Combine rows
Join all rows into one string
"""