# https://leetcode.com/problems/cutting-ribbons/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 1
        r = max(ribbons)
        ans = 0

        # Do the binary search now
        while l <= r:
            mid = (l + r) // 2

            if self.canCut(ribbons, k, mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans


    def canCut(self, ribbons: List[int], k: int, length: int) -> bool:
        cuts = 0

        for r in ribbons:
            cuts += r // length

        return cuts >= k

s = Solution()
assert(s.maxLength([9,7,5], 3) == 5)
assert(s.maxLength([7,5,9], 4) == 4)
assert(s.maxLength([5,7,9], 22) == 0)
assert(s.maxLength([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100000,1,1,1,1,1,1,1,1,1,1], 100049) == 1)
