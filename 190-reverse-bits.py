# https://leetcode.com/problems/reverse-bits/

# My solution. Too complicated, but it works.
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if 16 - i > 0: # shift left
                result = result | ((n & pow(2, i)) << ((16 - i) * 2 - 1))
            else: # shift right
                result = result | ((n & pow(2, i)) >> ((i - 16) * 2 + 1))
        
        return result

# After watching neetcode explanation.
class Solution2:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 -i))

        return result


s = Solution()

assert(s.reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000)
assert(s.reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111)