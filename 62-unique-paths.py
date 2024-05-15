# https://leetcode.com/problems/unique-paths/

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[None for y in range(m)] for x in range(n)]

        for i in range(m - 1, -1):
            for j in range(n - 1, -1):
                if i == (m - 1) and j == (n - 1):
                    cache[i][j] = 1
                elif j + 1 == n:
                    cache[i][j] = cache[i+1][j]
                elif i + 1 == m:
                    cache[i][j] = cache[i][j+1]
                else:
                    cache[i][j] = cache[i+1][j] + cache[i][j+1]
        
        return cache[0][0]
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]

s = Solution()

assert(s.uniquePaths(3, 7) == 28)
assert(s.uniquePaths(3, 2) == 3)
