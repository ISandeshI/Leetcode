# Directed Graph Cycle
# Graph Included
# Difficulty: MediumAccuracy: 27.88%Submissions: 580K+Points: 4
# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
# The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

# Examples:

# Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]



# Output: true
# Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0
# Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]


# Output: false
# Explanation: no cycle in the graph
# Constraints:
# 1 ≤ V ≤ 105
# 0 ≤ E ≤ 105
# 0 ≤ edges[i][0], edges[i][1] < V


from collections import defaultdict
class Solution:
    def isCyclic(self, V, edges):
        adjList = defaultdict(list)
        n = len(edges)
        for i in range(n):
            src = edges[i][0]
            dst = edges[i][1]
            adjList[src].append(dst)
        visited = [False] * V
        pathVisited = [False] * V

        def dfs(sourceNode):
            visited[sourceNode] = True
            pathVisited[sourceNode] = True

            for neighbour in adjList[sourceNode]:
                if pathVisited[neighbour]:
                    return True
                if visited[neighbour]:
                    continue
                if dfs(neighbour):
                    return True

            pathVisited[sourceNode] = False
            return False

        for j in range(V):
            if not visited[j]:
                if dfs(j):
                    return True
                
        return False


"""
Initialy i did wrong order of flow of code. I wrote:
                if visited[neighbour]:
                    continue
                if pathVisited[neighbour]:
                    return True

this made code skip valid paths beforehand, that's why i have to reverser order of this flow.

This is complete Shashcode's logic, i have nothing to do with this.
"""