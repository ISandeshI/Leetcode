# 441. Arranging Coins
# Easy
# Topics
# premium lock icon
# Companies
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def arrangeCoins(self, n: int):
        completeRows = 0
        currentCoin = 1
        while n > 0:
            if n >= currentCoin:
                n -= currentCoin
                currentCoin += 1
                completeRows += 1

            else:
                break
        return completeRows
    

"""
This has 724ms of runtime. 55%+ has 4ms of runtime. Which states above method is far worse.
In the begining i knew series formula will come to play. but to increase code efficiency
others have used BS with series formula:

Here by finding mid , we assume it may be number of rows, then using series formula we check
if mid is number of rows then how many coins there will be consumed. if it is equal to given 'n'
then it is answer, otherwise go left or right as per conditionand in the end return right.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            
            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right
"""