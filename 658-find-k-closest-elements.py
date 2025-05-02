# https://leetcode.com/problems/find-k-closest-elements/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&status=TO_DO&difficulty=MEDIUM%2CEASY&role=full-stack

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        # Now, binary search to find the closest value to x
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = (start + end) // 2
            if x - arr[mid] > arr[mid + k] - x:
                start = mid + 1
            else:
                end = mid

        return arr[start:start+k]

s = Solution()

assert(s.findClosestElements([1,3], 1, 2) == [1])
assert(s.findClosestElements([0,0,0,1,3,5,6,7,8,8], 2, 2) == [1,3])

assert(s.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5) == [3,3,4])
assert(s.findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4])
assert(s.findClosestElements([1,1,2,3,4,5], 4, -1) == [1,1,2,3])
