# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from typing import List

class DisjointedUnion():
    def __init__(self, size: int):
        self.graph = [0] * size
        for i in range(size):
            self.graph[i] = i

    def find(self, x):
        return self.graph[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.graph)):
                if self.graph[i] == rootY:
                    self.graph[i] = rootX

    def getComponentCount(self) -> int:
        tmp = set()

        for i in range(len(self.graph)):
            tmp.add(self.graph[i])

        return len(tmp)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Use an undirected graph
        # Flatten the path each time
        # At the end, return the count of distinct roots in graph
        du = DisjointedUnion(n)

        for x, y in edges:
            du.union(x, y)

        return du.getComponentCount()

s = Solution()


edges = [[0,1],[1,2],[3,4]]
assert(s.countComponents(5, edges) == 2)

edges = [[0,1],[1,2],[2,3],[3,4]]
assert(s.countComponents(5, edges) == 1)
