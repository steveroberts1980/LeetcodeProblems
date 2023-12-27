# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)):
            if needle[0] == haystack[i] and len(haystack) - len(needle) >= i:
                isMatch = True
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i+j]:
                        isMatch = False
                if isMatch:
                    return i
        return index
    
s = Solution()

assert s.strStr("sadbutsad", "sad") == 0
assert s.strStr("leetcode", "leeto") == -1
assert s.strStr("a", "a") == 0
