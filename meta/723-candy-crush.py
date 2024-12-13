# https://leetcode.com/problems/candy-crush/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])

        def getAdjacent() -> set:
            crushable = set()

            # first, check each vertical combo of 3
            for r in range(1, rows - 1):
                for c in range(cols):
                    if board[r][c] == 0:
                        continue
                
                    if board[r - 1][c] == board[r][c] == board[r + 1][c]:
                        crushable.update([(r-1,c),(r,c),(r+1,c)])

            for r in range(rows):
                for c in range(1, cols-1):
                    if board[r][c] == 0:
                        continue

                    if board[r][c-1] == board[r][c] == board[r][c+1]:
                        crushable.update([(r,c-1), (r,c), (r,c+1)])
                
            return crushable

        def drop():
            for c in range(cols):
                for r in range(rows):
                    if board[r][c] == 0:
                        cur_r = r
                        while cur_r > 0:
                            board[cur_r][c] = board[cur_r-1][c]
                            board[cur_r-1][c] = 0
                            cur_r -= 1

        locationsToCrush = getAdjacent()
        while locationsToCrush:
            for r, c in locationsToCrush:
                board[r][c] = 0

            # Now drop the candies
            drop()

            locationsToCrush = getAdjacent()

        return board


s = Solution()

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
result = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
assert(s.candyCrush(board) == result)

board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
result = [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
assert(s.candyCrush(board) == result)
