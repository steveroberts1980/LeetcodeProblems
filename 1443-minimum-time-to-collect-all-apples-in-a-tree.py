# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY%2CMEDIUM&status=TO_DO%2CATTEMPTED

from typing import List
from collections import defaultdict

class Solution:

    def dfs(self, node, parent, adj, hasApple):
        if node not in adj:
            return 0

        totalTime = 0
        childTime = 0

        for child in adj[node]:
            if child == parent:
                continue

            childTime = self.dfs(child, node, adj, hasApple)

            if childTime > 0 or hasApple[child]:
                totalTime += childTime + 2

        return totalTime

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)

        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]] = []

            if edge[1] not in adj[edge[0]]:
                adj[edge[0]].append(edge[1])

            if edge[1] not in adj:
                adj[edge[1]] = []

            if edge[0] not in adj[edge[1]]:
                adj[edge[1]].append(edge[0])

        return self.dfs(0, -1, adj, hasApple)


s = Solution()

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

assert(s.minTime(n, edges, hasApple) == 8)

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]

assert(s.minTime(n, edges, hasApple) == 6)
