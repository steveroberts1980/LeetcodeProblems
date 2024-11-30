# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        onePtr = 0
        twoPtr = len(nums) - 1

        i = 0

        def swap(index1, index2):
            tmp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = tmp

        while i <= twoPtr:
            if nums[i] == 0:
                swap(i, onePtr)
                onePtr += 1
                i += 1
            elif nums[i] == 2:
                swap(i, twoPtr)
                twoPtr -= 1
            else:  # value is 1
                i += 1

s = Solution()

nums = [2,0,2,1,1,0]
assert(s.sortColors(nums) == [0,0,1,1,2,2])

nums = [2,0,1]
assert(s.sortColors(nums) == [0,1,2])
