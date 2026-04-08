# 42. Trapping Rain Water
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxOnLeft = [0] * n
        maxOnRight = [0] * n
        water = [0] * n

        for i in range(n):
            if i == 0:
                maxOnLeft[i] = height[i]
            else:
                maxOnLeft[i] = max(maxOnLeft[i - 1], height[i])

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                maxOnRight[i] = height[i]
            else:
                maxOnRight[i] = max(maxOnRight[i + 1], height[i])

        for i in range(n):
            water[i]= min(maxOnLeft[i], maxOnRight[i]) - height[i]

        return sum(water)

"""
Runtime is 19ms beating only 17% + solutions and in memory beating 68% + solutions.
Do not refer this.
Logic was simple. You don't care about the tallest wall—only the shorter boundary that traps water.

At any index i, water stored depends on:
min(max height on left, max height on right) - height[i]

Why?
Water is bounded by the shorter wall.
Even if one side is very tall, water spills from the smaller side.
"""
