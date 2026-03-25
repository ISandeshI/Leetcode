# 901. Online Stock Span
# stack included
# Medium
# Topics
# premium lock icon
# Companies
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 

# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
 

# Constraints:

# 1 <= price <= 105
# At most 104 calls will be made to next.

class StockSpanner:

    def __init__(self):
        self.indexStack = []
        self.arr = []
        self.count = -1

    def next(self, price: int) -> int:
        self.count += 1
        self.arr.append(price)
        while self.indexStack and self.arr[self.indexStack[-1]] <= self.arr[self.count]:
            self.indexStack.pop()

        if not self.indexStack:
            ans = self.count + 1
        else:
            ans = self.count - self.indexStack[-1]

        self.indexStack.append(self.count)
        return ans

"""
Runtime 83ms Beating only 16.08% + solutions and in memory beating only 6.90% + solutions.
Please don't refer this. I just copied same code little bit modified according to current need, from 
GFG problem "stock span problem".

Following is brilliant solution by one of best users from LEETCODE, Answer is stored in tuple format
(price, span) and then appended to stack:

class StockSpanner:
    def __init__(self):
        self.stack=[]
         
    def next(self, price: int) -> int:
        span=1
        while len(self.stack):
            if self.stack[-1][0]>price:
                break
            span+=self.stack.pop()[1]
            
        self.stack.append((price, span)) 
        return span
"""