# 1791. Find Center of Star Graph
# Graph Included
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

# Example 1:


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
 

# Constraints:

# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashMap = Counter([num for sublist in edges for num in sublist])
        n = len(edges)
        for key, val in hashMap.items():
            if val == n:
                return key
            
"""
Runtime is 40ms beating only 23% + solutions and in memory beating only 7% + solutions.
this is worst solution. Don't refer it. Following is with 0ms Runtime:

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for u, v in edges:
            if u in seen:
                return u
            if v in seen:
                return v
            seen.add(u)
            seen.add(v)

OR

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]

        
"""