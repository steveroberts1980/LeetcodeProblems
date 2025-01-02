# https://leetcode.com/problems/isomorphic-strings/?envType=problem-list-v2&envId=hash-table



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            elif t[i] in mapping.values():
                return False
            else:
                mapping[s[i]] = t[i]

        return True



s = Solution()


assert(s.isIsomorphic("egg", "add"))
assert(not s.isIsomorphic("foo", "bar"))
assert(s.isIsomorphic("paper", "title"))
assert(not s.isIsomorphic("badc", "baba"))