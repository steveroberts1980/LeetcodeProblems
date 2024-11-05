# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def search(arr: List[int], left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2

            if arr[mid] < arr[mid+1]:
                return search(arr, mid+1, right)
            
            return search(arr, left, mid)

        return search(arr, 0, len(arr) - 1)

    def peakIndexInMountainArrayLinear(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while (left < right):
            mid = (left + right) // 2

            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid

        return left

s = Solution()

assert(s.peakIndexInMountainArrayLinear([0,1,0]) == 1)
assert(s.peakIndexInMountainArrayLinear([0,2,1,0]) == 1)
assert(s.peakIndexInMountainArrayLinear([0,10,5,2]) == 1)

