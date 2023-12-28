# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        ###
        # a, b > 0, abs(a) > abs(b) = positive answer
        # a < 0, b > 0, abs(a) > abs(b) = negative answer
        # a < 0, b > 0, abs(a) < abs(b) = positive answer
        # a < 0, b < 0, abs(a) > abs(b) = negative answer
        # a < 0, b < 0, abs(a) < abs(b) = negative answer
        #
        #
        #
        #
        ###

        sign = 1 if a > 0 else -1

        # Addition
        if a * b >= 0:
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry
        # Substraction
        else:
            while y:
                tmp = x ^ y 
                x, y = tmp, ((~x) & y) << 1

        return x * sign


s = Solution()

assert(s.getSum(-1, 1) == 0)
assert(s.getSum(9, 3) == 12)
assert(s.getSum(1, 2) == 3)
assert(s.getSum(2, 3) == 5)

