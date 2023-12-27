# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        numeralMap = {"CM": 900, "M": 1000, "CD": 400, "D": 500, "XC": 90, "C": 100, "XL": 40, "L": 50, "IX": 9,  "X": 10, "IV": 4, "V": 5, "I": 1 }

        retVal = 0
        while len(s) > 0:
            for n in numeralMap.keys():
                if s.startswith(n):
                    retVal += numeralMap[n]
                    s = s[len(n):]
                    break

        return retVal        

s = Solution()

assert(s.romanToInt("III") == 3)
assert(s.romanToInt("LVIII") == 58)
assert(s.romanToInt("MCMXCIV") == 1994)