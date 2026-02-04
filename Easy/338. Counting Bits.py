# 338. Counting Bits
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

class Solution:
    def countBits(self, n: int):
        list1 = []
        for i in range(n + 1):
            oneCount = 0
            while i  >  0:
                if i % 2 == 1:
                    oneCount += 1
                i //= 2
            list1.append(oneCount)
            
        return list1
        n.bit
    
"""
This turned out to be worse solution. it has 61ms of runtime.
Majority solutions have 1ms runtime.
We could have used readymade bin() function to solve this to write minumum code.
This runs in 7ms:

class Solution:
    def countBits(self, n: int):
        list1 = []
        for i in range(n + 1):
            list1.append(bin(i).count('1'))

        return list1
-----------------------------------------------------------------

Shortest answer: 
        l=[]
        for i in range(n+1):
            l.append(i.bit_count())
        return l

bit_count(): Number of ones in the binary representation of the absolute value of self


"""