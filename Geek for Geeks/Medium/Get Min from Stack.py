# Get Min from Stack
# stack included
# Difficulty: MediumAccuracy: 22.59%Submissions: 301K+Points: 4Average Time: 30m
# Implement a class SpecialStack that supports following operations:

# push(x) – Insert an integer x into the stack.
# pop() – Remove the top element from the stack.
# peek() – Return the top element from the stack. If the stack is empty, return -1.
# getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
# isEmpty() –  Return true if stack is empty, else false
# There will be a sequence of queries queries[][]. The queries are represented in numeric form:

# 1 x : Call push(x)
# 2:  Call pop()
# 3: Call peek()
# 4: Call getMin()
# 5: Call isEmpty()
# The driver code will process the queries, call the corresponding functions, and print the outputs of peek(), getMin(), isEmpty() operations.
# You only need to implement the above five functions.

# Examples:

# Input: q = 7, queries[][] = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
# Output: [3, 2, 1]
# Explanation: 
# push(2): Stack is [2]
# push(3): Stack is [2, 3]
# peek(): Top element is 3
# pop(): Removes 3, stack is [2]
# getMin(): Minimum element is 2
# push(1): Stack is [2, 1]
# getMin(): Minimum element is 1
# Input: q = 4, queries[][] = [[1, 4], [1, 2], [4], [3], [5]]
# Output: [2, 2, false]
# Explanation: 
# push(4): Stack is [4]
# push(2): Stack is [4, 2]
# getMin(): Minimum element is 2
# peek(): Top element is 2
# isEmpty(): false
# Constraints:
# 1 ≤ q ≤ 105
# 0 ≤ values on the stack ≤ 109

class SpecialStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min_val = x
        elif x >= self.min_val:
            self.stack.append(x)
        else:
            # store encoded value
            self.stack.append(2 * x - self.min_val)
            self.min_val = x

    def pop(self):
        if not self.stack:
            return -1

        top = self.stack.pop()

        if top >= self.min_val:
            return top
        else:
            # encoded value case
            original = self.min_val
            self.min_val = 2 * self.min_val - top
            return original

    def peek(self):
        if not self.stack:
            return -1

        top = self.stack[-1]

        if top >= self.min_val:
            return top
        else:
            # encoded value → actual value is min_val
            return self.min_val

    def isEmpty(self):
        return len(self.stack) == 0

    def getMin(self):
        if not self.stack:
            return -1
        return self.min_val

"""
Used AI for this solution. we could have solved this using two stacks, one for regular store and other 
for storing minium if found one. once element is popped then check it is also on the top of minstack.
if yes then also pop it and remaining top value is minimum for now.
This question is tricky just because we have to optimise the solution for minimum value.
We already know using min(stack) function will increase time complexity each time.
So someone come up with (2 * x - self.min_val) this encoded value.
It is similar to 155. Min Stack
"""