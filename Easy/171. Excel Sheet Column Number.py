# 171. Excel Sheet Column Number
# Easy
# Topics
# premium lock icon
# Companies
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
 

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
# -----------------------------------------------------------------------------------------------

#  so it is opposite of it's previous task, now convert column title to column number

class Solution:
    def titleToNumber(self, columnTitle: str):
        map = {
            "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
            "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
            "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26
        }

        count = 0
        strLength = len(columnTitle) - 1
        for i in columnTitle:
            count += map[i] * (26**strLength)
            strLength -= 1

        return count
    
"""
Above code runs in 0ms.
If you remember previously we have to convert 1-25 into 0-25 because
Z is represented by 0 in modulo operation.

Above code works because you are NOT using modulo (% 26) at all.
You are treating Excel columns as a pure base-26 number system with digits 1–26, not 0–25.

So no adjustment is needed.
"""
