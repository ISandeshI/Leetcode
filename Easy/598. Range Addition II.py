# 598. Range Addition II
# Easy
# Topics
# premium lock icon
# Companies
# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.

 

# Example 1:


# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
# Example 2:

# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
# Example 3:

# Input: m = 3, n = 3, ops = []
# Output: 9
 

# Constraints:

# 1 <= m, n <= 4 * 104
# 0 <= ops.length <= 104
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        
        minX = ops[0][0]
        minY = ops[0][1]
        for row in ops:
            minX = min(minX, row[0])
            minY = min(minY, row[1])

        return minX * minY
    
"""
Used Chatgpt for debugging. This runs in 0ms.

Why Brute Force is Unnecessary
What brute force would do
Create an m * n matrix

For every operation [a, b]:
Increment all cells from (0,0) to (a-1, b-1)
Scan matrix to find max value and count it

Why this is bad

Matrix size can be huge
Time: O(m * n * len(ops))
Memory: O(m * n)
Totally impractical

The Key Observation (THIS kills brute force)
Every operation:
always starts from (0,0)


So:

Cells closer to (0,0) get incremented more times
Cells outside some operation’s range get incremented fewer times
The maximum value appears only where all operations overlap

That's the reason to choose minimum of ops[0] and ops[1]
and return it's multiplication
"""