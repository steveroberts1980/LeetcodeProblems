# https://leetcode.com/problems/koko-eating-bananas/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTimeToEat(bananas_per_hour: int) -> int:
            time = 0
            for p in piles:
                time += (math.ceil(p / bananas_per_hour))

            return time

        # First, determine the upper bound
        upper = max(piles)

        # Second, determine the lower bound
        lower = 1

        # Then binary search to find the optimal time
        while lower < upper:
            mid = (lower + upper) // 2

            time_to_eat = getTimeToEat(mid)

            if time_to_eat <= h:
                upper = mid
            else:
                lower = mid + 1

        return lower

s = Solution()

print(s.minEatingSpeed([312884470], 968709470))
assert(s.minEatingSpeed([3,6,7,11], 8) == 4)
assert(s.minEatingSpeed([30,11,23,4,20], 5) == 30)
assert(s.minEatingSpeed([30,11,23,4,20], 6) == 23)