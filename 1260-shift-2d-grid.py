# https://leetcode.com/problems/shift-2d-grid/

from typing import List, Tuple

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Convert placement to a single array position
        # Add k to the position and mod with total number of places in grid
        # Convert placement back to grid position
        result = [[0] * len(grid[0]) for _ in range(len(grid))]
        itemCount = len(grid) * len(grid[0])
        numCols = len(grid[0])

        def getArrayPosition(r, c) -> int:
            return r * numCols + c

        def getGridPosition(index) -> Tuple[int, int]:
            row = index // numCols
            col = index - (row * numCols)
            return (row, col)
    
        tmp = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                pos = getArrayPosition(r, c)
                pos = (pos + k) % itemCount 
                new_r, new_c = getGridPosition(pos)
                result[new_r][new_c] = grid[r][c]
        
        return result


s = Solution()

grid = [[1,2,3],[4,5,6],[7,8,9]]
result = [[9,1,2],[3,4,5],[6,7,8]]

assert(s.shiftGrid(grid, 1) == result)

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
result = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

assert(s.shiftGrid(grid, 4) == result)

grid = [[1,2,3],[4,5,6],[7,8,9]]
result = [[1,2,3],[4,5,6],[7,8,9]]

assert(s.shiftGrid(grid, 9) == result)