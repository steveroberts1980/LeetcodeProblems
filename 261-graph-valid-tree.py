# https://leetcode.com/problems/graph-valid-tree/

from typing import List

class disjointUnion():
    def __init__(self, size):
        self.graph = [0] * size
        for i in range(size):
            self.graph[i] = i

    def find(self, x):
        return self.graph[x]

    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # These have already been recorded.
        
        for i in range(len(self.graph)):
            if self.graph[i] == rootY:
                self.graph[i] = rootX
    
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        du = disjointUnion(n)
        for x, y in edges:
            if not du.union(x, y):
                return False
            
        # Now check to ensure there is only 1 root
        count = 0
        for i in range(n):
            if du.graph[i] == i:
                count += 1
            if count > 1:
                return False
            
        return True



s = Solution()

edges = [[0,1],[0,2],[0,3],[1,4]]
assert(s.validTree(5, edges))

edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
assert(not s.validTree(5, edges))