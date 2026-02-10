# Aggressive Cows
# Difficulty: MediumAccuracy: 59.57%Submissions: 196K+Points: 4Average Time: 30m
# You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

# Examples:

# Input: stalls[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at stalls[0], 
# the second cow can be placed at stalls[2] and 
# the third cow can be placed at stalls[3]. 
# The minimum distance between cows in this case is 3, which is the largest among all possible ways.
# Input: stalls[] = [10, 1, 2, 7, 5], k = 3
# Output: 4
# Explanation: The first cow can be placed at stalls[0],
# the second cow can be placed at stalls[1] and
# the third cow can be placed at stalls[4].
# The minimum distance between cows in this case is 4, which is the largest among all possible ways.
# Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
# Output: 1
# Explanation: There are 6 stalls and only 5 cows, we try to place the cows such that the minimum distance between any two cows is as large as possible.
# The minimum distance between cows in this case is 1, which is the largest among all possible ways.
# Constraints:
# 2 ≤ stalls.size() ≤ 106
# 0 ≤ stalls[i] ≤ 108
# 2 ≤ k ≤ stalls.size()

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low = stalls[1] - stalls[0]
        high = stalls[-1] - stalls[0]
        ans = high

        while low <= high:
            mid = (low + high) // 2

            count = k - 1
            prevCow = 0
            for i in range(1, len(stalls)):
                if stalls[i] - stalls[prevCow] >= mid:
                    prevCow = i
                    count -= 1

            if count > 0:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans
 
"""
Took approach from ai, my code didn't work so still used AI.
i thought low would be distance between 2nd and 1st element, but i was wrong.
What low ACTUALLY means in binary search

low is not:
the smallest gap between stalls
low is:
the smallest possible answer we want to test
Binary search must cover ALL valid answers.


"""