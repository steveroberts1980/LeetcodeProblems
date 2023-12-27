from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        i = int(len(nums) / 2)

        return min(self.findMin(nums[0:i]), self.findMin(nums[i:len(nums)]))

s = Solution()

assert(s.findMin([3,4,5,1,2]) == 1)
assert(s.findMin([4,5,6,7,0,1,2]) == 0)
assert(s.findMin([11,13,15,17]) == 11)