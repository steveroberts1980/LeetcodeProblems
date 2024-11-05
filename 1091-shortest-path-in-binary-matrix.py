# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Use BFS
        directions = [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def get_neighbors(row: int, col: int):
            neighbors = []

            for d in directions:
                n_row = row + d[0]
                n_col = col + d[1]
                if n_row >= 0 and n_row < len(grid) and n_col >= 0 and n_col < len(grid[0]):
                    if grid[n_row][n_col] == 0:
                        neighbors.append((n_row, n_col))
        
            return neighbors

        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1
        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]

            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return distance
            
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1
                queue.append((neighbor_row, neighbor_col))

        return -1


s = Solution()

grid = [[0,1],[1,0]]

assert(s.shortestPathBinaryMatrix(grid) == 2)

grid = [[0,0,0],[1,1,0],[1,1,0]]

assert(s.shortestPathBinaryMatrix(grid) == 4)

grid = [[1,0,0],[1,1,0],[1,1,0]]

assert(s.shortestPathBinaryMatrix(grid) == -1)