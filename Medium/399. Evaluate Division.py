from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graphHashmap = defaultdict(list)
        for i in range(len(equations)):
            source, destination = equations[i][0], equations[i][1]
            graphHashmap[source].append((destination, values[i]))
            graphHashmap[destination].append((source, 1 / values[i]))

        ans = []
        
        def dfs(src, dest, multiplicationTillYet, visitedNodes):
            if src not in graphHashmap or dest not in graphHashmap:
                return -1
            # this question demands if node is not present in equations then just give -1, 
            # even if in queries both nodes are same and not present in equations
            
            if src == dest:
                return multiplicationTillYet
            
            visitedNodes.add(src)

            for currNeighbour, weight in graphHashmap[src]:
                if currNeighbour not in visitedNodes:
                    result = dfs(currNeighbour, dest, multiplicationTillYet * weight, visitedNodes)

                    if result != -1:
                        return result
                
            return -1
                 

        for sr, dst in queries:
            visited = set()
            ans.append(dfs(sr, dst, 1, visited))

        return ans
    
"""
Runtime is 0ms and in memory beating only 12% + solutions.
This is actually hard problem, I have cheked neetcode's solution and implemented same.

"""