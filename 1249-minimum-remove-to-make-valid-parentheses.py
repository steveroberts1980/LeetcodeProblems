class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Keep a stack of left parens.
        # As long as there is a left paren on the stack when we get a right paren,
        # then keep the right paren and then pop the left.
        # once the string is built, reverse it and do it again.

        def prune(s, open: str, close: str):
            retVal = []
            count = 0
            for i in range(len(s)):
                if s[i] == open:
                    count += 1
                    retVal.append(s[i])
                elif s[i] == close:
                    if count:
                        count -= 1
                        retVal.append(s[i])
                else:
                    retVal.append(s[i])
        
            return "".join(retVal), count
        
        s, count = prune(s, "(", ")")

        if count:
            s = s[::-1]
            s, _ = prune(s, ")", "(")
            s = s[::-1]

        return s

sol = Solution()

assert(sol.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de")
assert(sol.minRemoveToMakeValid("a)b(c)d") == "ab(c)d")
assert(sol.minRemoveToMakeValid("))((") == "")