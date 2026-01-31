# 119. Pascal's Triangle II
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
class Solution:
    def getRow(self, rowIndex: int):
        outList = []
        prevList = [1]
        for i in range(rowIndex + 1):
            outList.append(prevList)
            nextList= []
            nextLength = i + 2
            for j in range(nextLength):
                if j - 1 < 0:
                    prevLeft = 0
                else:
                    prevLeft = prevList[j-1]
                if j >= len(prevList):
                    prevRight= 0
                else:
                    prevRight = prevList[j]

                currentNum = prevLeft + prevRight
                nextList.append(currentNum)

            prevList = nextList

        return outList[-1]
    

"""
Before solving i knew this would give late runtime, it has 4ms runtime.
More than 85% of submissions have 0ms runtime.

I just used the same logic as in problem 118 and returned the last row only.
In this code there is one unneccesary list outList which stores all the rows.
It is not needed here as we only need the last row. That's why the runtime is more.

"""