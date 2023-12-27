class Solution:
    def climbStairs(self, n: int) -> int:

        return self.climbStairsRecurse(n, 0)

    def climbStairsRecurse(self, n: int, spot: int):
        if spot == n:
            return 1
        
        if spot > n:
            return 0
        
        return self.climbStairsRecurse(n, spot + 1) + self.climbStairsRecurse(n, spot + 2)
            

# TODO - This is not passing. Time limit is getting exceeded.

s = Solution()
#print(s.climbStairs(38))
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3

