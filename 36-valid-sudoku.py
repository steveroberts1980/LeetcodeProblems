# https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=hash-table

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First check each row and column
        for i in range(len(board)):
            row_nums = set()
            col_nums = set()
            for j in range(len(board[0])):
                if board[i][j] in row_nums:
                    return False
                
                if board[j][i] in col_nums:
                    return False
                
                if board[j][i] != '.':
                    col_nums.add(board[j][i])

                if board[i][j] != '.':
                    row_nums.add(board[i][j])

        # Finally, check each square
        for i in range(len(board) // 3):
            for j in range(len(board[0]) // 3):
                nums = set()
                # Check the nine squares
                for r in range(3*i, 3*i+3):
                    for c in range(3*j, 3*j+3):
                        if board[r][c] in nums:
                            return False
                        
                        if board[r][c] != '.':
                            nums.add(board[r][c])

        return True



s = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#assert(s.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#assert(not s.isValidSudoku(board))

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

assert(not s.isValidSudoku(board))