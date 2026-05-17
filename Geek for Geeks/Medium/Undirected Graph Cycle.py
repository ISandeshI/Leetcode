# Undirected Graph Cycle
# Graph Included
# Difficulty: MediumAccuracy: 30.13%Submissions: 719K+Points: 4Average Time: 20m
# Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

# Note: The graph can have multiple component.

# Examples:

# Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: true
# Explanation: 
 
# 1 -> 2 -> 0 -> 1 is a cycle.
# Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
# Output: false
# Explanation: 
 
# No cycle in the graph.
# Constraints:
# 1 ≤ V, E ≤ 105
# 0 ≤ edges[i][0], edges[i][1] < V

from collections import deque,defaultdict
class Solution:
	def isCycle(self, V, edges):
        visited = [False] * V
        edges1 = defaultdict(list)
        for source, destination in edges:
            edges1[source].append(destination)
            edges1[destination].append(source)
        
        def bfs(currentNode, parent):
            queue = deque()
            queue.append((currentNode, parent)) #inserting as tuple (node, parent)
            visited[currentNode] = True
            while queue:
                n = len(queue)
                for i in range(n):
                    currentNode1, parent1 = queue.popleft()
                    for neighbour in edges1[currentNode1]:
                        if neighbour == parent1:
                            continue
                        if visited[neighbour]:
                            return True
                        else:
                            visited[neighbour] = True
                            queue.append((neighbour, currentNode1))
            
            return False                       

        for j in range(V):
            if not visited[j]:
                if bfs(j, -1):
                    return True
				
        return False
		
"""
It alsmost took me a month to solve this problem, eventualy gave up and use shashcode's logic.
Watch video for explaination:
https://www.youtube.com/watch?v=gvNeSmWatIc
"""