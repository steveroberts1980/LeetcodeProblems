# https://leetcode.com/problems/next-permutation/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Start from the right side
        # We have 3 cases:
        # 1. All are sorted ascending
        # 2. All are sorted descending
        # 3. Not sorted
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = len(nums) - 2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)

        # now reverse the remaining numbers
        start = i + 1
        end = len(nums) - 1
        while start < end:
            swap(nums, start, end)
            start += 1
            end -= 1

s = Solution()

nums = [1,2,3]

s.nextPermutation(nums)

assert(nums == [1,3,2])

nums = [3,2,1]

s.nextPermutation(nums)

assert(nums == [1,2,3])

nums = [1,1,5]

s.nextPermutation(nums)

assert(nums == [1,5,1])
        