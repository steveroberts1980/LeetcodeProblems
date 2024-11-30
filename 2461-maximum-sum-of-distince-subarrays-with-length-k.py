# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        val = sum = 0
        end = k
        hash = {}

        for i in range(k):
            sum += nums[i]
            hash[nums[i]] = hash.get(nums[i], 0) + 1
        
        if len(hash.keys()) == k:
            val = max(val, sum)

        while end < len(nums):
            start = end-k
            sum -= nums[start]
            sum += nums[end]

            hash[nums[start]] -= 1
            if hash[nums[start]] == 0:
                del hash[nums[start]]

            hash[nums[end]] = hash.get(nums[end], 0) + 1

            if len(hash.keys()) == k:
                val = max(val, sum)

            end += 1

        return val

s = Solution()

assert(s.maximumSubarraySum([1,2,2], 2) == 3)
assert(s.maximumSubarraySum([5,3,3,1,1], 3) == 0)
assert(s.maximumSubarraySum([1,5,4,2,9,9,9], 3) == 15)
assert(s.maximumSubarraySum([4,4,4], 3) == 0)
