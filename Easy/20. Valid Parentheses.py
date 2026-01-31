# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s):
        mapping = {
                    ")" : "(",
                    "]" : "[",
                    "}" : "{"
                }

        stack = []
        for ch in s:
            if ch in mapping:

                if (not stack or mapping[ch] != stack[-1]):
                    return False

                stack.pop()


            else:
                stack.append(ch)

        if not stack:
            return True

        else:
            return False
        


"""
i made some stupid mistake. on line 66 initially i wrote:
if (mapping[ch] != stack[-1] or not stack):
 here if stack is empty then stack[-1] will give index error. i wrote the conditions in wrong order.
 so i have to reverse the conditions. we should first check if stack is empty or not.

 i have resubmitted the code and it is accepted now. above version is also correct but 
 it takes 3ms more, becase in the end on line 75 we have
  if else condition to check if stack is empty or not.

 if we watch this carefully all these 4 lines can be converted into single line:
    return not stack

    this line will check if stack is empty or not and return True or False accordingly.

"""