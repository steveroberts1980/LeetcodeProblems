# https://leetcode.com/problems/counting-bits/

from typing import List

class SolutionFirst:
    def countBits(self, n: int) -> List[int]:
        retVal = []

        def hammingWeight(n: int) -> int:
            counter = 0

            while n:
                counter += n & 1
                n = n >> 1
        
            return counter
        
        for i in range(n+1):
            retVal.append(hammingWeight(i))

        return retVal

class Solution:
    def countBits(self, n: int) -> List[int]:
        retVal = []
        retVal.append(0)
        msb = 1

        for i in range(1, n + 1):
            if msb * 2 == i:
                msb = i

            retVal.append(1 + retVal[i - msb])

        return retVal

s = Solution()

assert(s.countBits(2) == [0,1,1])
assert(s.countBits(5) == [0,1,1,2,1,2])

