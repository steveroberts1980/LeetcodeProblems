# https://leetcode.com/problems/string-to-integer-atoi/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

class Solution:
    def myAtoi(self, s: str) -> int:
        ret_val = 0
        positive = True
        num_started = False
        
        for i in range(len(s)):
            if s[i].isdigit():
                num_started = True
                if s[i] == "0" and ret_val == 0:
                    continue
                ret_val = (ret_val * 10) + int(s[i])
            elif num_started:
                break
            elif s[i] in ["+", "-"]:
                num_started = True
                if s[i] == "-":
                    positive = False
            elif s[i] == " ":
                continue
            elif not s[i].isdigit():
                break
   
        if positive:
            ret_val = min(ret_val, pow(2, 31) - 1)
        else:
            ret_val = max(-1 * ret_val, -1 * pow(2, 31))

        return ret_val

s = Solution()

#assert(s.myAtoi("42") == 42)
#assert(s.myAtoi("-042") == -42)
assert(s.myAtoi("1337c0d3") == 1337)
assert(s.myAtoi("0-1") == 0)
assert(s.myAtoi("words and 987") == 0)