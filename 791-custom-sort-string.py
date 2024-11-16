# https://leetcode.com/problems/custom-sort-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_chars = {}
        output = list()

        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1

        for c in order:
            cnt = s_chars.get(c, 0)
            if cnt:
                for i in range(cnt):
                    output.append(c)
                del s_chars[c]
            
        # Now append the remaining characters in the hash to the output
        for c in s_chars.keys():
            for i in range(s_chars[c]):
                output.append(c)

        return "".join(output)
        
s = Solution()

assert(s.customSortString("cba", "abcd") == "cbad")
assert(s.customSortString("bcafg", "abcd") == "bcad")


