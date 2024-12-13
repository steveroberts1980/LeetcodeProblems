# https://leetcode.com/problems/continuous-subarray-sum/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixMod = 0
        modSeen = {}

        modSeen[0] = -1

        for i in range(len(nums)):
            prefixMod = (prefixMod + nums[i]) % k

            if prefixMod in modSeen:
                if i - modSeen[prefixMod] > 1:
                    return True
            else:
                modSeen[prefixMod] = i

        return False


s  = Solution()

assert(s.checkSubarraySum([23,2,4,6,7], 6))
assert(s.checkSubarraySum([23,2,6,4,7], 6))
assert(not s.checkSubarraySum([23,2,6,4,7], 13))
