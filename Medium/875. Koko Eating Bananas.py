# 875. Koko Eating Bananas
# Medium
# Topics
# premium lock icon
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 
# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            hoursTaken = 0

            for i in piles:
                hoursTaken += math.ceil(i / mid)

            if hoursTaken <= h: 
                #means we maybe eating too fast, current mid is in right side, so let's check in left part
                high = mid -1
                ans = mid

            else:
                low = mid + 1

        return ans



"""
I Will be honest, i did not even understand the question. Yet this answer took 178ms of runtime.
Then after understanding i did not even come up with any possible solution for it.
Eventualy i search on chatgpt.

hoursTaken += math.ceil(i / mid) this line can be written as:
hoursTaken += (i + mid - 1) / mid

So the solution is binary search. This problem is solved using binary search on the answer. 
The key observation is that as Koko's eating speed increases, the total number of hours 
required decreases monotonically. We binary search the minimum speed between 1 and the maximum pile size.
For each candidate speed, we calculate how many hours it would take by summing the 
ceiling of pile / speed for each pile, since Koko can eat from only one pile per hour and partial piles 
still take a full hour. Based on whether the total hours exceed h, we adjust the search range 
until we find the smallest valid speed.
"""