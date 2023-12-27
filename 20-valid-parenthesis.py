# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opps = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in range(len(s)):
            if s[i] in opps.values():
                stack.append(s[i])
            else:
                if stack.count == 0:
                    return False
                
                if opps[s[i]] != stack.pop():
                    return False

        return len(stack) == 0

s = Solution()
assert(s.isValid("()"))
assert(s.isValid("()[]{}"))
assert(not s.isValid("(]"))