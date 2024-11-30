# https://leetcode.com/problems/verifying-an-alien-dictionary/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create the array of list orders using a hash and the order int

        # Next, compare words 2 at a time, moving through the list from left to right
        # As long as letters are the same, continue comparing letters. If any letters on the right are 
        # before letters on the left, return false.
        # If any letters in the left word remain after comparing all the letters, then return false

        d = {}

        for c in order:
            d[c] = len(d)

        for i in range(len(words)- 1): # Don't go to the end, since we will get the current index word and the next one.
            w1 = words[i]
            w2 = words[i+1]
            isValid = False

            for pos in range(min(len(w1), len(w2))):
                if d[w2[pos]] < d[w1[pos]]:
                    return False

                if d[w2[pos]] > d[w1[pos]]:
                    isValid = True
                    break # The right word is in the right order. Just go on to the next word

            if len(w1) > len(w2) and not isValid:
                return False

        return True



s = Solution()

assert(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
assert(not s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
assert(not s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))