# https://leetcode.com/problems/minesweeper/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

# BFS

from typing import List

class Solution:
    adjacents = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    visited = set()

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        return self.markSpaces(board, click[0], click[1])

    def markSpaces(self, board: List[List[str]], x, y):
        # If square has adjacent mines, change to the number of adjacent mines.
        if (x, y) in self.visited:
            return board
        
        self.visited.add((x, y))

        mines = self.adjacentMines(board, x, y)

        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for (adj_x, adj_y) in self.adjacentSquares(board, x, y):
                board = self.markSpaces(board, adj_x, adj_y)

        return board

    def adjacentSquares(self, board: List[List[str]], x, y):
        board_x = len(board)
        board_y = len(board[0])
        adj = []

        for a in self.adjacents:
            adj_x = x + a[0]
            adj_y = y + a[1]
            if adj_x >= 0 and adj_x < board_x and adj_y >= 0 and adj_y < board_y and (adj_x, adj_y) not in self.visited:
                adj.append((adj_x, adj_y))

        return adj

    def adjacentMines(self, board: List[List[str]], x, y) -> int:
        board_x = len(board)
        board_y = len(board[0])
        mines = 0
        for a in self.adjacents:
            adj_x = x + a[0]
            adj_y = y + a[1]
            if adj_x >= 0 and adj_x < board_x and adj_y >= 0 and adj_y < board_y and board[adj_x][adj_y] == 'M':
                mines += 1
        
        return mines


s = Solution()

# board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
# output = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
# assert(s.updateBoard(board, [3,0]) == output)

# board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
# output = [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
# assert(s.updateBoard(board, [1,2]) == output)

board = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
output = [["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]
ans = s.updateBoard(board, [0,0])
print(ans)
assert(ans == output)