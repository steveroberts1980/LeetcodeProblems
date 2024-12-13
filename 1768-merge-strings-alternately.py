# https://leetcode.com/problems/merge-strings-alternately/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[minLength:])
        merged.append(word2[minLength:])
        
        return "".join(merged)


s = Solution()

assert(s.mergeAlternately("abc", "pqr") == "apbqcr")
assert(s.mergeAlternately("ab", "pqrs") == "apbqrs")
assert(s.mergeAlternately("abcd", "pq") == "apbqcd")

