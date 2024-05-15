# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

# DFS Solution
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass

# DP Solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1]*len(nums)

        # Check the rest of the indexes. 
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + cache[j])

        max_sub = 0

        for val in cache:
            max_sub = max(max_sub, val)

        return max_sub


s = Solution()

assert(s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
assert(s.lengthOfLIS([0,1,0,3,2,3]) == 4)
assert(s.lengthOfLIS([7,7,7,7,7,7,7]) == 1)

