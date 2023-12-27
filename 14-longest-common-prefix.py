class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallestWord = 201

        for s in strs:
            smallestWord = min(len(s), smallestWord)

        for i in range(smallestWord):
            tmp = strs[0][i]

            for s in strs[1:]:
                if s[i] != tmp:
                    tmp = ""
                    break

            if tmp == "":
                break

            prefix += tmp

        return prefix        

s = Solution()

assert(s.longestCommonPrefix(["flower","flow","flight"]) == "fl")
assert(s.longestCommonPrefix(["dog","racecar","car"]) == "")
