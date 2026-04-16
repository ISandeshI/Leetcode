# 856. Score of Parentheses
# stack included
# Medium
# Topics
# premium lock icon
# Companies
# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2
 

# Constraints:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack[-1]
                if val == 0:
                    stack[-1] = 1
                else:
                    while len(stack) > 1 and stack[-2] != 0:
                        val1 = stack.pop()
                        val2 = stack.pop()
                        stack.append(val1 + val2)

                    val3 = stack.pop()
                    if stack:
                        stack[-1] = 2 * val3
                    else:
                        stack.append(val3)

        return sum(stack)
    

"""
Runtime is 0ms and in memory beating 89% + solutions.
Day by day with practise i am getting dumb, i am one of the rarest kind who is degrading with practise.
this took me 3 days to solve and also i made this overcomplicated.
Following is smartest solution:

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * val
        
        return stack[0]
"""