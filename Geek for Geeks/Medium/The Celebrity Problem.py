# The Celebrity Problem
# Difficulty: MediumAccuracy: 38.33%Submissions: 372K+Points: 4Average Time: 30m
# A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

# Note: Follow 0-based indexing.

# Examples:

# Input: mat[][] = [[1, 1, 0],
#                 [0, 1, 0],
#                 [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.
# Input: mat[][] = [[1, 1], 
#                 [1, 1]]
# Output: -1
# Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.
# Input: mat[][] = [[1]]
# Output: 0
# Constraints:
# 1 ≤ mat.size() ≤ 1000
# 0 ≤ mat[i][j] ≤ 1
# mat[i][i] = 1

class Solution:
    def celebrity(self, mat):
        row = len(mat) 
        col = row
        count = 0

        for i in range(row):
            for j in range(col):
                if mat[j][i] == 0:
                    count = 0
                    break
                count += 1
            if count == row and mat[i].count(1) == 1:
                return i
        return -1
    
"""
too much brute force, so we should not use this solution.
There are so many way for this code, we chose this one.
"""
        