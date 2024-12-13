# https://leetcode.com/problems/course-schedule/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List
from collections import defaultdict, deque

class disjointedUnion():
    def __init__(self, size):
        self.graph = [0] * size
        for i in range(size):
            self.graph[i] = i

    def find(self, x):
        return self.graph[x]

    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY: # the requested union will create a cycle
            return False

        if rootX != rootY:
            for i in range(len(self.graph)):
                if self.graph[i] == rootY:
                    self.graph[i] = rootX


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        du = disjointedUnion(numCourses)

        for x, y in prerequisites:
            if not du.union(x, y):
                return False
            
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()

        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1


        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodesVisited = 0

        while q:
            node = q.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return nodesVisited == numCourses
    
class Solution3:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True

s = Solution3()

assert(s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
assert(s.canFinish(2, [[1,0]]))
assert(not s.canFinish(2, [[1,0], [0,1]]))
