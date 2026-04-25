# 2285. Maximum Total Importance of Roads
# Graph Included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

# You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

# Return the maximum total importance of all roads possible after assigning the values optimally.

 

# Example 1:


# Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
# Output: 43
# Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
# - The road (0,1) has an importance of 2 + 4 = 6.
# - The road (1,2) has an importance of 4 + 5 = 9.
# - The road (2,3) has an importance of 5 + 3 = 8.
# - The road (0,2) has an importance of 2 + 5 = 7.
# - The road (1,3) has an importance of 4 + 3 = 7.
# - The road (2,4) has an importance of 5 + 1 = 6.
# The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
# It can be shown that we cannot obtain a greater total importance than 43.
# Example 2:


# Input: n = 5, roads = [[0,3],[2,4],[1,3]]
# Output: 20
# Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
# - The road (0,3) has an importance of 4 + 5 = 9.
# - The road (2,4) has an importance of 2 + 1 = 3.
# - The road (1,3) has an importance of 3 + 5 = 8.
# The total importance of all roads is 9 + 3 + 8 = 20.
# It can be shown that we cannot obtain a greater total importance than 20.
 

# Constraints:

# 2 <= n <= 5 * 104
# 1 <= roads.length <= 5 * 104
# roads[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no duplicate roads.

from collections import Counter
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hashMap = Counter([num for sublist in roads for num in sublist])
        sortedHashMap = dict(sorted(hashMap.items(), key = lambda item: item[1], reverse = True))
        # 1st index has frequency, and we want reverse sorted

        result = 0

        for key, val in sortedHashMap.items():
            result += (val * n)
            n -= 1

        return result
    
"""
Runtime is 86ms beating 42% + solutions and in memory beating only 9% + solutions.
This is worst solution because we are doing a lot of operations like list creation, then hashmap creation,
then sorting this hashmap, then last for loop.
Following is shortest and fast solution(runtime 20ms):

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for c1, c2 in roads:
            degrees[c1] += 1
            degrees[c2] += 1
        degrees.sort()

        max_importance = 0
        value = 1
        for degree in degrees:
            max_importance += value * degree
            value += 1
        return max_importance
"""