# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        
        if x <= 3:
            return 1
        
        ceil = int(x/2)
        floor = 1

        while ceil > floor:
            if ceil * ceil == x:
                return ceil
            elif ceil * ceil > x:
                ceil = int(ceil - ((ceil - floor) / 2))
            else:
                oldFloor = floor
                floor = int(ceil)
                ceil = int(ceil + (ceil - oldFloor))
        
        return floor
    
    def mySqrt2(self, x: int) -> int:

        if x == 0:
            return 0
        
        if x <= 3:
            return 1
        
        return int(self.mySqrt2a(x, 1, int(x/2)))

    def mySqrt2a(self, x: int, floor: int, ceil: int) -> int:
        if ceil * ceil == x:
            return ceil
        elif ceil <= floor:
            return floor
        elif ceil * ceil > x:
            return self.mySqrt2a(x, int(floor), int(ceil - ((ceil - floor) / 2)))
        elif ceil * ceil < x:
            return self.mySqrt2a(x, int(ceil), int(ceil + (ceil - floor)))

s = Solution()

assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(pow(2, 31)) == 46340