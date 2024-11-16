# https://leetcode.com/problems/subarray-sum-equals-k/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = sum = 0
        map = {}
        map[0] = 1

        for i in range(len(nums)):
            sum += nums[i]

            if (sum - k) in map:
                counter += map.get(sum - k)
            map[sum] = map.get(sum, 0) + 1
        
        return counter

s = Solution()

assert(s.subarraySum([1,1,1], 2) == 2)
assert(s.subarraySum([1,2,3], 3) == 2)