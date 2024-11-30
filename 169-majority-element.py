# https://leetcode.com/problems/majority-element/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        maxCount = 0
        majorityElement = 0

        for n in nums:
            tmp = counts.get(n, 0) + 1
            counts[n] = tmp
            if tmp > maxCount:
                maxCount = tmp
                majorityElement = n
        
        return majorityElement


s = Solution()

assert(s.majorityElement([3,2,3]) == 3)
assert(s.majorityElement([2,2,1,1,1,2,2]) == 2)
