# Histogram Max Rectangular Area
# stack included
# Difficulty: HardAccuracy: 32.12%Submissions: 210K+Points: 8
# You are given a histogram represented by an array arr[ ], where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

# Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

# Examples:

# Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
#  Largest-Rectangular-Area-in-a-Histogram
# Output: 100
# Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
# Input: arr[] = [3, 5, 1, 7, 5, 9]
# Output: 15
# Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.
# Input: arr[] = [3]
# Output: 3
# Explanation: In this example the largest area would be 3 of height 3 and width 1.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 104

class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        leftSmaller = [-1] * n
        rightSmaller = [n] * n
        stackLeft = []
        stackRight = []
        maxArea = 0

        for i in range(n):
            while stackLeft and arr[stackLeft[-1]] >= arr[i]:
                stackLeft.pop()

            if stackLeft:
                leftSmaller[i] = stackLeft[-1]

            stackLeft.append(i)

        for i in range(n - 1, -1, -1):
            while stackRight and arr[stackRight[-1]] >= arr[i]:
                stackRight.pop()

            if stackRight:
                rightSmaller[i] = stackRight[-1]

            stackRight.append(i)

        for i in range(n):
            maxArea = max(maxArea, (rightSmaller[i] - leftSmaller[i] - 1) * arr[i])

        return maxArea
    
"""
You could have used same stack for both of loops with emptying it between them.
This took me a lot of time to correct.
basic approach is to find left and right boundry for current element with smaller element.
this is how we calculate it's width and then according to curent height we can calculate current area.
check for each height, what could be max area then compute answer accordingly.

"""