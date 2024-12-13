# https://leetcode.com/problems/rotting-oranges/

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_oranges = set()
        max_time = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_oranges.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        
        valid_neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            i, j, time = q.popleft()
            max_time = max(time, max_time)

            for x, y in valid_neighbors:
                new_x = i + x
                new_y = j + y

                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    good_oranges.remove((new_x,new_y))
                    grid[new_x][new_y] = 2
                    q.append((new_x, new_y, time+1))

        if good_oranges:
            return -1

        return max_time

s = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
assert(s.orangesRotting(grid) == 4)

grid = [[2,1,1],[0,1,1],[1,0,1]]
assert(s.orangesRotting(grid) == -1)

grid = [[0,2]]
assert(s.orangesRotting(grid) == 0)
