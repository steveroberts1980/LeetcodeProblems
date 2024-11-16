# https://leetcode.com/problems/number-of-1-bits/

######################################
# Bit manipulation
######################################

class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 32
        counter = 0

        while x:
            counter += n & 1
            n = n >> 1
            x -= 1
    
        return counter

s = Solution()

assert(s.hammingWeight(0b00000000000000000000000000001011) == 3)
assert(s.hammingWeight(0b00000000000000000000000010000000) == 1)
assert(s.hammingWeight(0b11111111111111111111111111111101) == 31)
