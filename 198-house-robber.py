# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sumAtIndex = [None] * len(nums)

        def robHome(index) -> int:
            if index >= len(nums):
                return 0

            if sumAtIndex[index] != None:
                return sumAtIndex[index]

            sumAtIndex[index] = max(robHome(index + 1), robHome(index + 2) + nums[index])
            return sumAtIndex[index]

        return robHome(0)
    
s = Solution()

assert(s.rob([1,2,3,1]) == 4)
assert(s.rob([2,7,9,3,1]) == 12)
