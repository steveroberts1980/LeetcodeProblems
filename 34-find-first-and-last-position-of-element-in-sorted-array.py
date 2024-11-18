# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0
        end = len(nums) - 1
        first = last = -1

        if not nums:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            return [-1, -1]

        # find first index
        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] == target:
                if mid == begin or nums[mid -1] != target:
                    first = mid
                    break
                else:
                    end = mid - 1
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1

        # now reset and find last index
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] == target:
                if mid == end or nums[mid + 1] != target:
                    last = mid
                    break
                else:
                    begin = mid + 1
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1        

        return [first, last]


s = Solution()

s.searchRange([2,2], 3)
#print(s.searchRange([5,7,7,8,8,10], 8))
#print(s.searchRange([5,7,7,8,8,10], 7))
assert(s.searchRange([5,7,7,8,8,10], 8) == [3,4])
assert(s.searchRange([5,7,7,8,8,10], 6) == [-1,-1])
assert(s.searchRange([], 0) == [-1,-1])

