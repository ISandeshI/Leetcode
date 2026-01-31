# 118. Pascal's Triangle
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int):
        outList = []
        prevList = [1]
        for i in range(numRows):
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

        return outList


"""
I swear to god, i did not took any help from the internet to solve this problem.
and thought this will take time.
I did not just solve this but it has 0ms runtime.

i made a an error like range(len(numRows)) in line 28 but fixed it quickly.
Here numRows is an integer not a list. So could not use len() function on it.

"""