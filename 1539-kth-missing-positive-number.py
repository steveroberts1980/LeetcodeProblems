# https://leetcode.com/problems/kth-missing-positive-number/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack&status=TO_DO%2CATTEMPTED

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set()
        ret_val = 0

        for num in arr:
            nums.add(num)

        i = 0
        counter = 0
        while i != k:
            counter += 1
            if counter not in nums:
                i += 1
            
        return counter


s = Solution()

assert(s.findKthPositive([1,2], 1) == 3)
assert(s.findKthPositive([2,3,4,7,11], 5) == 9)
assert(s.findKthPositive([1,2,3,4], 2) == 6)

