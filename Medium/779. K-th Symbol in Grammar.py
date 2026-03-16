# 779. K-th Symbol in Grammar
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01
# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation: 
# row 1: 0
# row 2: 01
 

# Constraints:

# 1 <= n <= 30
# 1 <= k <= 2n - 1

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        length = 2**(n - 1)
        mid = length // 2
        
        if n == 1:
            return 0
        
        if k <= mid:
            return self.kthGrammar(n - 1, k)

        else:
           return 1 - self.kthGrammar(n - 1, k - mid)
            


"""
Runtime is 0ms and in memory it is beating 86% + solutions.
what was key idea?

consider row 3 = 0110
         row 4 = 01101001

if you notice, for each current row, first half of it's content is equal to exact copy of it's previous row.
And second half of current row is opposite copy of it's previous row.

So recursion idea is, check if k is upto middle, then go to previous row's kth element.
And if k is more than half, then go to previous row's (k - mid) copy and do the not value of it.
Here (k - mid) is mirror position in previous row.

"""