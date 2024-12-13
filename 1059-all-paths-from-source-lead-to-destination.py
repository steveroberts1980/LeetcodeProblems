# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

from typing import List
from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Construct graph
        graph = defaultdict(list)

        for start, end in edges:
            graph[start].append(end)

        # The destination node has outgoing edges.
        if graph[destination]:
            return False
        
        # DFS base case will be if ending node is destination.
        def dfs(node, visited = set()):
            if not graph[node]:
                return node == destination

            if node in visited:
                return False            

            visited.add(node)

            for n in graph[node]:
                if not dfs(n, visited):
                    return False

            visited.remove(node)

            return True

        return dfs(source)



s = Solution()

edges = [[5,15],[38,34],[29,5],[6,32],[46,2],[34,22],[2,25],[1,18],[10,10],[26,46],[40,46],[36,19],[16,13],[46,6],[19,32],[7,41],[14,32],[20,13],[0,43],[17,14],[42,41],[40,12],[28,7],[36,35],[18,2],[28,11],[14,32],[4,9],[26,6],[7,17],[49,41],[17,2],[36,34],[18,0],[26,15],[27,10],[26,46],[41,14],[47,19],[19,14],[6,3],[16,14],[21,43],[4,15],[5,2],[31,2],[5,30],[7,33],[18,2],[9,33],[21,44],[1,43],[37,17],[8,24],[21,33],[46,45],[29,14],[22,32],[14,14],[22,32],[42,6],[7,14],[35,13],[36,35],[5,25],[2,3],[23,22],[44,33],[24,13],[35,19],[20,14],[14,32],[35,5],[44,13],[32,32],[32,32],[28,46],[32,32],[37,10],[38,46],[30,30],[0,3],[15,9],[39,15],[42,44],[2,20],[47,0],[49,44],[45,4],[36,22],[13,13],[14,30],[13,14],[31,31],[45,3],[45,5],[34,14],[44,9],[30,30],[40,12],[13,30],[25,20],[34,14],[41,22],[12,34],[5,33],[20,22],[48,5],[48,7],[46,0],[14,32],[32,30],[38,46],[30,30],[35,15],[37,20],[42,2],[26,13],[8,48],[20,30],[37,33],[28,18],[32,30],[10,10],[48,44],[24,14],[8,9],[0,14],[1,43],[14,14],[20,22],[31,10],[1,0],[4,7],[27,41],[41,22],[0,22],[17,19],[8,16],[18,38],[37,23],[5,22],[35,23],[14,30],[30,30],[13,32],[28,23],[24,25],[45,2],[25,22]]
n = 50
source = 15
destination = 33
assert(s.leadsToDestination(n, edges, source, destination))

n = 3
edges = [[0,1],[0,2]]
source = 0
destination = 2
assert(not s.leadsToDestination(n,edges,source,destination))

n = 4
edges = [[0,1],[0,3],[1,2],[2,1]]
source = 0
destination = 3
assert(not s.leadsToDestination(n,edges,source,destination))

n = 4
edges = [[0,1],[0,2],[1,3],[2,3]]
source = 0
destination = 3
assert(s.leadsToDestination(n,edges,source,destination))

