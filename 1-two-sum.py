from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash and hash[diff] != i:
                return [i, hash[diff]]

s = Solution()

assert(s.twoSum([2,7,11,15], 9) == [0,1])
assert(s.twoSum([3,2,4], 6) == [1,2])
assert(s.twoSum([3,3], 6) == [0,1])
