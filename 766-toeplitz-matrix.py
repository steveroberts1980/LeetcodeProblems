# https://leetcode.com/problems/toeplitz-matrix/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # Would need to check diagonals from the top row of starting numbers.
        # We can skip the last element since it will always be true
        # Then, check the diagonals going down the left side. We can skip the first and last 
        # since the last will always be true and the first will have been checked in the top row

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        if num_cols == 1 or num_rows == 1:
            return True
        
        for i in range(0, num_cols):
            start = matrix[0][i]
            r = 1
            c = i + 1

            while r < num_rows and c < num_cols:
                if matrix[r][c] != start:
                    return False
                
                r += 1
                c += 1

        for i in range(1, num_rows):
            start = matrix[i][0]
            r = i + 1
            c = 1

            while r < num_rows and c < num_cols:
                if matrix[r][c] != start:
                    return False
                
                r += 1
                c += 1

        return True


s = Solution()

assert(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
assert(not s.isToeplitzMatrix([[1,2],[2,2]]))