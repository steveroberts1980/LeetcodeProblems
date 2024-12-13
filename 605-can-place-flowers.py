# https://leetcode.com/problems/can-place-flowers/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 1
        numFlowers = 0

        for i in flowerbed:
            if i:
                numFlowers += (max(0, counter - 1) // 2)
                counter = 0
            else:
                counter += 1

        numFlowers += (max(0, counter) // 2)

        return numFlowers >= n


s = Solution()

assert(s.canPlaceFlowers([1,0,0,0,1], 1))
assert(not s.canPlaceFlowers([1,0,0,0,1], 2))