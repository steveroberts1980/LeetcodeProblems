# https://leetcode.com/problems/maximum-product-subarray/description/

######################################
# Dynamic Programming
######################################

from typing import List
import math


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_product = current_max
        
        for i in range(1, len(nums)):

            temp_max = max(nums[i], current_max * nums[i], current_min * nums[i])
            current_min = min(nums[i], current_min * nums[i], current_max * nums[i])

            current_max = temp_max
            
            max_product = max(max_product, current_max)

        return max_product


s = Solution()

assert(s.maxProduct([2,3,-2,4]) == 6)
assert(s.maxProduct([-2,0,-1]) == 0)


