# https://leetcode.com/problems/group-shifted-strings/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&status=TO_DO%2CATTEMPTED&difficulty=EASY%2CMEDIUM

from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def getSequence(s: str) -> tuple:
            if len(s) == 1:
                return (-1)

            sequence = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i-1]) + 26) % 26
                sequence.append(diff)

            return tuple(sequence)

        for s in strings:
            seq = getSequence(s)
            groups[seq].append(s)

        return list(groups.values())


s = Solution()

print(s.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(s.groupStrings(["a"]))
