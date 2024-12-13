# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        graph = defaultdict(list)
        stack = []
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack.append(source)
        visited.add(source)

        while stack:
            curr_node = stack.pop()
            if curr_node == destination:
                return True
            
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return False
                



s = Solution()

# edges = [[0,1],[1,2],[2,0]]
# assert(s.validPath(3, edges, 0, 2))

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
assert(not s.validPath(6, edges, 0, 5))
