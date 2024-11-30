# https://leetcode.com/problems/search-a-2d-matrix-ii/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Recursively search the submatrices. 
        # Can jump right out of a subsearch by checking the values at the corners
        # since the data is sorted.
        if not matrix:
            return False
        
        def search(left, right, top, bottom) -> bool:
            if left > right or top > bottom:
                return False
            
            if matrix[top][left] > target or matrix[bottom][right] < target:
                return False
            
            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            
            return search(left, mid_col, top, mid_row) or search(mid_col + 1, right, top, mid_row) or search(left, mid_col, mid_row + 1, bottom) or search(mid_col + 1, right, mid_row + 1, bottom)

        mid_row = len(matrix) // 2
        mid_col = len(matrix[0]) // 2
        
        return search(0, mid_col, 0, mid_row) or search(mid_col + 1, len(matrix[0]) -1, 0, mid_row) or search(0, mid_col, mid_row + 1, len(matrix) -1) or search(mid_col + 1, len(matrix[0]) -1, mid_row + 1, len(matrix) -1)

s = Solution()

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

assert(s.searchMatrix(matrix, 19))

matrix = [[1,4],[2,5]]

assert(s.searchMatrix(matrix, 2))

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

assert(s.searchMatrix(matrix, 5))

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

assert(not s.searchMatrix(matrix, 20))
