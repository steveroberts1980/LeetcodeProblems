# https://leetcode.com/problems/unique-paths/

# class Solution2:
#     def uniquePaths(self, m: int, n: int) -> int:
#         cache = [[None for y in range(m)] for x in range(n)]

#         for i in range(m - 1, -1):
#             for j in range(n - 1, -1):
#                 if i == (m - 1) and j == (n - 1):
#                     cache[i][j] = 1
#                 elif j + 1 == n:
#                     cache[i][j] = cache[i+1][j]
#                 elif i + 1 == m:
#                     cache[i][j] = cache[i][j+1]
#                 else:
#                     cache[i][j] = cache[i+1][j] + cache[i][j+1]
        
#         return cache[0][0]
    
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         row = [1] * n

#         for i in range(m - 1):
#             newRow = [1] * n
#             for j in range(n - 2, -1, -1):
#                 newRow[j] = newRow[j + 1] + row[j]
#             row = newRow

#         return row[0]




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Can take a recursive approach here as
        # at every space, the robot can move right or down
        # so this is essentially binary search tree  
        cache = [[0 for y in range(n)] for x in range(m)]
        cache[m-1][n-1] = 1

        for i in range(n):
            cache[m-1][i] = 1

        for i in range(m):
            cache[i][n-1] = 1

        for i in range(m-1):
            for j in range(n-1):
                x = m - 2 - i
                y = n - 2 - j
                cache[x][y] = cache[x+1][y] + cache[x][y+1]
            
        return cache[0][0]





s = Solution()

assert(s.uniquePaths(3, 7) == 28)
assert(s.uniquePaths(3, 2) == 3)
