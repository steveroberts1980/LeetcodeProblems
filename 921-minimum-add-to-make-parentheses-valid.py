# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # We can push opening parens onto a stack. Every time we come to a
        # closing paren, pop one off the stack. If there are none on the stack,
        # then our closing would have needed an opening to make it valid, so increment our 
        # counter
        # At the end, add any open parens that were not closed out. 

        count = 0
        openCount = 0

        for char in s:
            if char == "(":
                openCount += 1
            else:
                if openCount:
                    openCount -= 1
                else:
                    count += 1

        return count + openCount


s = Solution()

assert(s.minAddToMakeValid("())") == 1)
assert(s.minAddToMakeValid("(((") == 3)

