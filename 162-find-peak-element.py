# https://leetcode.com/problems/find-peak-element/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO%2CATTEMPTED&role=full-stack

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums: List[int], start, end):
            if start == end:
                return start
            
            mid = (start + end) // 2

            if nums[mid] > nums[mid+1]:
                return search(nums, start, mid)
            
            return search(nums, mid+1, end)

        return search(nums, 0, len(nums)-1)



s = Solution()

assert(s.findPeakElement([1,2,3,1]) == 2)
assert(s.findPeakElement([1,2,1,3,5,6,4]) in [1, 5])