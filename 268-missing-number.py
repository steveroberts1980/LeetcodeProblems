# https://leetcode.com/problems/missing-number/

from typing import List

# My solution. 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remainder = 0

        for i in range(len(nums)):
            remainder += i + 1
            remainder -= nums[i]

        return remainder
    

s = Solution()

assert(s.missingNumber([3,0,1]) == 2)
assert(s.missingNumber([0,1]) == 2)
assert(s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8)

