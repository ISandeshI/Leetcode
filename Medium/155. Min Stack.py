# 155. Min Stack
# stack included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.minVal = val
            self.stack.append(val)

        else:
            if val >= self.minVal:
                self.stack.append(val)
            else:
                newInt = 2 * val - self.minVal
                self.stack.append(newInt)    
                self.minVal = val

    def pop(self) -> None:
        lastElement = self.stack.pop()
        if lastElement < self.minVal:
            self.minVal = 2 * self.minVal - lastElement
        

    def top(self) -> int:
        lastElement = self.stack[-1]
        if lastElement < self.minVal:
            return self.minVal
        else:
            return lastElement

    def getMin(self) -> int:
        return self.minVal



"""
Runtime is 1ms beating 87% + solutons and in memory beating 74% + solutions.
similar problem already seen in GFG:Get Min from Stack.
Same logic.

while pushing we have to remember formula:
    newInt = 2 * val - self.minVal
and while popping we need to remember:
    self.minVal = 2 * self.minVal - lastElement

without these formulas we cannot do anything. So you have to have yuour mathematical knowldge for this 
to sove such kind of problems
"""