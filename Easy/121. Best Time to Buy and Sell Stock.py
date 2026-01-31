# 121. Best Time to Buy and Sell Stock
# Easy
# Topics
# premium lock icon
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
class Solution:
    def maxProfit(self, prices: List[int]):
        highestProfit = 0
        lowestValue = prices[0]

        for i in range(1,len(prices)):
            lowestValue = min(lowestValue, prices[i])
            highestProfit = max(highestProfit, prices[i] - lowestValue)

        return highestProfit






"""
Above solution has 66ms runtime. so much worst, many of other solutions did better than this.

we used min() and max() which are readymade functions continously, thats why it has more runtime. 
If we had used if else statements comparing minimum and maximum then runtime would have decreased to 2ms.

Following get TLE because it has O(n^2) complexity due to nested loop.
That's the reason we had used above solution which make n passes only.
Approach is different, from begining keep track of minimum as well, and then check the 
highest profit by finding highest value in further indexes.

class Solution:
    def maxProfit(self, prices: List[int]):
        highestProfit = 0
        for i in range(len(prices) - 1):
            j = i + 1
            while j < len(prices):
                highestProfit = max(highestProfit, prices[j] - prices[i])
                j += 1

        return highestProfit

"""