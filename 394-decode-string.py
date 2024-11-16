# https://leetcode.com/problems/decode-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM




class Solution:
    def decodeString(self, s: str) -> str:
        parts = []
        multiplier_stack = []
        i = 0
        part = ""

        while i < len(s):
            if s[i].isdigit():
                # parse the digit
                num, i = self.get_num(s, i)
                multiplier_stack.append((num, ''))

            if s[i] == ']':
                # pop the multiplier and create the string part
                # if the stack is empty, then add the completed part to the parts array 
                # and clear the part
                multiplier, part = multiplier_stack.pop()
                part = part * multiplier

                if not multiplier_stack:
                    parts.append(part)
                    part = ""
                else:
                    multiplier, parent_part = multiplier_stack.pop()
                    parent_part += part
                    multiplier_stack.append((multiplier, parent_part))
            elif s[i] != '[': # must be a character
                if multiplier_stack:
                    num, part = multiplier_stack.pop()
                    part += s[i]
                    multiplier_stack.append((num, part))
                else:
                    parts.append(s[i])

            i += 1

        return "".join(parts)


    def get_num(self, s: str, i: int) -> tuple[int, int]:
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        return (num, i)
        


s = Solution()

assert(s.decodeString("3[a]2[bc]") == "aaabcbc")
assert(s.decodeString("3[a2[c]]") == "accaccacc")
assert(s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")