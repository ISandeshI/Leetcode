# 70. Climbing Stairs
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45


class Solution:
    def climbStairs(self, n: int):
        ways = 0
        data = {}
        def feb(m):
            if m in data:
                return data[m]
            if m ==0 or m == 1:
                return 1
            else:
                data[m] = feb(m - 1) + feb(m - 2)
                return data[m]
            
        if n > 1:
            ways = feb(n)
            return ways

        else:
            return 1
        


"""
Above solution is optimized using memoization.
Runtime is 0ms which is faster than 100% of python3 submissions.
To be honest i did not know the solution to this problem initially.
i thought of solving using permutations and combinations.
But this thinking led to nowhere.

So i searched for the solution and found that this is a fibonacci problem.

To reach step n, you must come from:

step n-1 (by taking 1 step), or

step n-2 (by taking 2 steps)

So the number of ways to reach step n is:

ways (n) = ways (n−1) + ways (n−2)

This is exactly the Fibonacci sequence.

But remember:

Base Cases are:
ways(0) = 1 → one way (do nothing)
ways(1) = 1 → only one step

--------------------------------------------------------------------------


my previous solution:
class Solution:
    def climbStairs(self, n: int):
        ways = 0
        def feb(m):
            if m ==0 or m == 1:
                return 1
            else:
                return feb(m - 1) + feb(m - 2)
            
        if n > 1:
            ways = feb(n)
            return ways

        else:
            return 1


here you can see i have not used dictionary to store the previous results.
this caused time limit exceeded error for large inputs.
although the logic is correct but it is not optimized.
so i have used dictionary to store the previous results and check 
if the result is already computed or not.

"""


