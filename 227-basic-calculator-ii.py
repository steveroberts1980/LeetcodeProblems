# https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def calculate(self, s: str) -> int:
        
        def calc(s: str) -> int:
            s = s.strip()

            isNegative = s[0] == '-'

            if isNegative:
                s = s[1:]

            if s.isdigit():
                if isNegative:
                    return int(s) * -1
                
                return int(s)

            # addition case
            tmp = s.split('+', 1)
            if len(tmp) > 1:
                if isNegative:
                    return calc('-'+tmp[0]) + calc(tmp[1])
                else:
                    return calc(tmp[0]) + calc(tmp[1])
            
            # substraction case
            tmp = s.split('-', 1)
            if len(tmp) > 1:
                if isNegative:
                    return calc('-'+tmp[0]) + calc('-'+tmp[1])
                else:
                    return calc(tmp[0]) + calc('-'+tmp[1])
            
            # multiplication case
            tmp = s.split('*', 1)
            if len(tmp) > 1:
                if isNegative:
                    return calc('-'+tmp[0]) * calc(tmp[1])
                else:
                    return calc(tmp[0]) * calc(tmp[1])

            # division case
            tmp = s.split('/', 1)
            if len(tmp) > 1:
                if isNegative:
                    return int('-'+calc(tmp[0]) / calc(tmp[1]))
                else:
                    return int(calc(tmp[0]) / calc(tmp[1]))

        return calc(s)


s = Solution()

assert(s.calculate("12-3*4") == 0)
assert(s.calculate("1-1-1") == -1)
assert(s.calculate("3+2*2") == 7)
assert(s.calculate(" 3/2 ") == 1)
assert(s.calculate(" 3+5 / 2 ") == 5)
