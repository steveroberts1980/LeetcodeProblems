# https://leetcode.com/problems/word-break/description/

######################################
# TODO
######################################

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    cache[i] = cache[i + len(w)]

                if cache[i]:
                    break

        return cache[0]


s = Solution()

assert(s.wordBreak("leetcode", ["leet", "code"]))
assert(s.wordBreak("applepenapple", ["apple", "pen"]))
assert(not s.wordBreak("catsandog", ["cats", "sand", "and", "cat"]))