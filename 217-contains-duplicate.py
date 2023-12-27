from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = 1
            
        return False

s = Solution()


assert(s.containsDuplicate([1,2,3,1]))
assert(not s.containsDuplicate([1,2,3,4]))
assert(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

