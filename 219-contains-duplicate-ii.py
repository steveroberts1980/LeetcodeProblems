# https://leetcode.com/problems/contains-duplicate-ii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&status=TO_DO&difficulty=EASY%2CMEDIUM&role=backend

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valueHash = {}

        for i in range(len(nums)):
            if nums[i] in valueHash and abs(i - valueHash[nums[i]]) <= k:
                return True
            valueHash[nums[i]] = i

        return False



s = Solution()

assert(s.containsNearbyDuplicate([1,2,3,1], 3))
assert(s.containsNearbyDuplicate([1,0,1,1], 1))
assert(not s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
