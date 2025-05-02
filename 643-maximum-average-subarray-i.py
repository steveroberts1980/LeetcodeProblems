# https://leetcode.com/problems/maximum-average-subarray-i/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        maxAvg = 0

        for i in range(k):
            sum += nums[i]

        maxAvg = sum  / float(k)

        i = k
        while i < len(nums):
            sum += nums[i]
            sum -= nums[i - k]
            maxAvg = max(maxAvg, sum / float(k))
            i += 1

        return maxAvg


s = Solution()

nums = [1,12,-5,-6,50,3]
k = 4

assert(s.findMaxAverage(nums, k) == 12.75)

assert(s.findMaxAverage([5], 1) == 5.00)

