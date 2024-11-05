# https://leetcode.com/problems/random-pick-with-weight/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO%2CATTEMPTED&role=full-stack

from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.lookup = {}
        self.total = 0

        for i in range(0, len(w)):
            self.total += w[i]
            self.lookup[self.total] = i

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)

        for i in self.lookup:
            if rand <= i:
                return self.lookup[i]


s = Solution([1])
print(s.pickIndex())

s = Solution([1,3])
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
