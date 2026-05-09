# <!-- BFS of graph
# Graph Included
# Difficulty: EasyAccuracy: 44.09%Submissions: 556K+Points: 2Average Time: 10m
# Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

# Note: Do traverse in the same order as they are in the given adjacency list.

# Examples:

# Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

# Output: [0, 2, 3, 1, 4]
# Explanation: Starting from 0, the BFS traversal will follow these steps: 
# Visit 0 → Output: 0 
# Visit 2 (first neighbor of 0) → Output: 0, 2 
# Visit 3 (next neighbor of 0) → Output: 0, 2, 3 
# Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 1
# Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4
# Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

# Output: [0, 1, 2, 3, 4]
# Explanation: Starting from 0, the BFS traversal proceeds as follows: 
# Visit 0 → Output: 0 
# Visit 1 (the first neighbor of 0) → Output: 0, 1 
# Visit 2 (the next neighbor of 0) → Output: 0, 1, 2 
# Visit 3 (the first neighbor of 2 that hasn't been visited yet) → Output: 0, 1, 2, 3 
# Visit 4 (the next neighbor of 2) → Final Output: 0, 1, 2, 3, 4
# Constraints:
# 1 ≤ V = adj.size() ≤ 104
# 0 ≤ adj[i][j] ≤ 104


from collections import deque
class Solution:
    def bfs(self, adj):
        n = len(adj)
        queue = deque()
        visited = [0] * n
        result = []

        for i in range(n):
            if not visited[i]:
                queue.append(i)
                while queue:
                    lenght = len(queue)
                    for j in range(lenght):
                        vertice = queue.popleft()
                        if not visited[vertice]:
                            visited[vertice] = 1
                            result.append(vertice)
                            for k in range(len(adj[vertice])):
                                if not visited[adj[vertice][k]]:
                                    queue.append(adj[vertice][k])

        return result
    
"""
Without anyone's logic i write this on my own. That's the reason it is not optimised.
finding length of queue for level traversal is logic from tree. It is not needed here.
But if level tracking is required then we need length calculation for queue.
Following is optimised code:

from collections import deque

class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [0] * n
        result = []

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = 1

                while queue:
                    node = queue.popleft()
                    result.append(node)

                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = 1
                            queue.append(neighbor)

        return result


"""