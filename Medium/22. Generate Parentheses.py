# 22. Generate Parentheses
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recursion(string, leftRemaining, rightRemaining):
            if leftRemaining == 0 and rightRemaining == 0:
                ans.append(string)

            if leftRemaining > 0:
                recursion(string + "(", leftRemaining - 1, rightRemaining)

            if rightRemaining > leftRemaining:
                recursion(string + ")", leftRemaining, rightRemaining - 1)

        recursion("", n, n)

        return ans
    
"""
Runtime 2ms beating only 34% + solurions (most have 0ms runtime) and in memory beating 66% + solutions.

"""