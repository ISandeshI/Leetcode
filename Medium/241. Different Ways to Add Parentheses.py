# 241. Different Ways to Add Parentheses
# DP Included
# Medium
# Topics
# premium lock icon
# Companies
# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        hashMap = {}
        operators = "+-*"
        
        def backtracking(start, end):
            if expression[start:end + 1] in hashMap:
                return hashMap[expression[start:end + 1]]
            
            ans = []
            if (end - start) < 2:
                num = int(expression[start:end + 1])
                ans.append(num)
                hashMap[expression[start:end + 1]] = ans
                return ans
            
            for i in range(start, end + 1):
                if expression[i] not in operators:
                    continue

                left = backtracking(start, i - 1)
                right = backtracking(i + 1, end)

                for num1 in left:
                    for num2 in right:
                        if expression[i] == "+":
                            ans.append(num1 + num2)
                        if expression[i] == "-":
                            ans.append(num1 - num2)
                        if expression[i] == "*":
                            ans.append(num1 * num2)

            hashMap[expression[start:end + 1]] = ans
            return ans
        
        return backtracking(0, len(expression) - 1)

"""
Runtime is 0ms and in memory beating 99% + solutions.
I saw video of shashcode, took his approach of solving, and interestingly my code turned out to be most 
perfect. I don't take any credit.
For explaination, watch:
https://www.youtube.com/watch?v=0titnH6hL5A

"""