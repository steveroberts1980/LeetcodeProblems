# https://leetcode.com/problems/number-of-provinces/

from typing import List

class disjointedUnion():
    def __init__(self, length):
        self.vertices = [0] * length
        for i in range(length):
            self.vertices[i] = i

    def find(self, x):
        return self.vertices[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.vertices)):
                if self.vertices[i] == rootY:
                    self.vertices[i] = rootX

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        du = disjointedUnion(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    du.union(i, j)

        provinces = set()

        for i in range(len(du.vertices)):
            provinces.add(du.vertices[i])

        return len(provinces)
    
s = Solution()

# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# assert(s.findCircleNum(isConnected) == 2)

# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# assert(s.findCircleNum(isConnected) == 3)

isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
assert(s.findCircleNum(isConnected) == 3)

