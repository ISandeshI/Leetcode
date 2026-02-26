# 812. Largest Triangle Area
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
 

# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

from typing import List
import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Line coefficients
                A = y2 - y1
                B = x1 - x2
                C = x2*y1 - x1*y2
                
                base = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    x3, y3 = points[k]
                    
                    # Perpendicular height
                    height = abs(A*x3 + B*y3 + C) / math.sqrt(A*A + B*B)
                    
                    area = 0.5 * base * height
                    
                    max_area = max(max_area, area)
        
        return max_area


"""
Don't refer this it is among worst with runtime 146ms beating 11% + solutions and in memory beating only 32% +
solutions. It is among simplest soutions out there. Logic:

Find longest base and height, then area = ½ × base × height”

This thinking is correct in geometry…

But the problem is:

👉 The longest X-distance and longest Y-distance may NOT form a triangle together.
👉 The height must be perpendicular to the chosen base.
👉 Bounding box extremes do not guarantee a valid triangle.


✅ Correct “Base + Height” Approach (Pure Geometry)

For every pair of points:

Treat them as a base.
Compute base length using distance formula.
For every third point:
Compute perpendicular height from that point to the base line.
Compute area.
Keep maximum.
📐 How to Compute Height Without Cross Product?
Distance from point C(x3,y3) to line AB:
Line equation method:
If:

A(x1, y1)
B(x2, y2)


Line form: Ax+By+C=0

Where:

A = y2 - y1
B = x1 - x2
C = x2*y1 - x1*y2


Distance formula:

height=∣Ax3+By3+C∣/sqrt(A^2+B^2)

--------------------------------------------------------------------------------

Use following code instead, you have to have knowledge of determinant / cross product formula.
Area of triangle using 3 points:

If points are:

A(x1, y1)
B(x2, y2)
C(x3, y3)

Area= (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|

Since constraints are small (n ≤ 50):
Pick every combination of 3 points.
Compute area.
Keep track of maximum.

So complexity becomes O(n^3), which is acceptable in this case.

import itertools

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        
        for A, B, C in itertools.combinations(points, 3):
            x1, y1 = A
            x2, y2 = B
            x3, y3 = C
            
            area = abs(
                x1*(y2 - y3) +
                x2*(y3 - y1) +
                x3*(y1 - y2)
            ) / 2
            
            max_area = max(max_area, area)
        
        return max_area


if you don't want to use itertool then use manual looping:

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    
                    area = abs(
                        x1*(y2 - y3) +
                        x2*(y3 - y1) +
                        x3*(y1 - y2)
                    ) / 2
                    
                    max_area = max(max_area, area)
        
        return max_area


itertool is faster with suntime of 39ms beating 69% + solutions and manual looping has 
runtime of 43ms beating 51% + solutions.
"""