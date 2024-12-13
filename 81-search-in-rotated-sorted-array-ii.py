# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Start with a binary search. Then we will need to adjust for the cases.
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        if not nums:
            return False
        
        if len(nums) == 1:
            return nums[0] == target 

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            
            if nums[start] == nums[mid]:
                start += 1
                continue

            # Need to update for the cases on a rotated array. 
            # For now, assume the array has no duplicates.
            if nums[mid] > nums[start]:
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False

s = Solution()

assert(s.search([2,5,6,0,0,1,2], 0))
assert(not s.search([2,5,6,0,0,1,2], 3))

