# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if len(logs) <  (n - 1):
            return -1

        du = [0] * n
        count = n - 1

        for i in range(n):
            du[i] = i

        def find(x):
            return du[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                du[i] = rootX
                for i in range(len(du)):
                    if du[i] == rootY:
                        du[i] = rootX
                
                return 1
            return 0
        
        logs.sort()
        for timestamp, x, y in logs:
            count -= union(x, y)

            if not count:
                return timestamp
            
        return -1


s = Solution()

logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
n = 4
print(s.earliestAcq(logs, n))

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6

assert(s.earliestAcq(logs, n) == 20190301)

logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
n = 4

assert(s.earliestAcq(logs, n) == 3)

