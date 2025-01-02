# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    numerals = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    numeral_vals = [1000, 500, 100, 50, 10, 5, 1]
    subtractive_vals = [900, 400, 90, 40, 9, 4]

    def intToRoman(self, num: int) -> str:
        result = []

        while num > 0:
            tmp = str(num)

            if tmp[0] not in ["4", "9"]:
                for i in self.numeral_vals:
                    if i <= num:
                        result.append(self.numerals[i])
                        num -= i
                        break
            else:
                for i in self.subtractive_vals:
                    if i <= num:
                        result.append(self.numerals[i])
                        num -= i
                        break

        return "".join(result)


s = Solution()

#print(s.intToRoman(1994))

assert(s.intToRoman(3749) == "MMMDCCXLIX")
assert(s.intToRoman(58) == "LVIII")
assert(s.intToRoman(1994) == "MCMXCIV")
