# 1482. Minimum Number of Days to Make m Bouquets
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
# Example 2:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
# Example 3:

# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.
 

# Constraints:

# bloomDay.length == n
# 1 <= n <= 105
# 1 <= bloomDay[i] <= 109
# 1 <= m <= 106
# 1 <= k <= n

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int):
        totalFolwerNeeded = m * k
        if totalFolwerNeeded > len(bloomDay):
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        while low <= high:
            mid = (low + high) // 2

            bouquet = 0
            consecutive = 0
            for i in bloomDay:
                if i <= mid:
                    consecutive += 1
                    if consecutive == k:
                        bouquet += 1
                        consecutive = 0
                else:
                    consecutive = 0

            if bouquet >= m:
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1

        return ans
    

"""
This runs in 300ms yet it beats 71% solutions.
I figured out that this can be solved with BS. But the middle logic which is very simple above
where we check how many bouquets we can make at given time, is taken from chatgpt.
I tried sliding window, obviously it was never going to work. I got TLE by that.
so after struggling for more than 3 hours for this problem i used AI.
"""