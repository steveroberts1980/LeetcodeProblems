from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Left subarray is sorted
            if nums[left] < nums[mid - 1]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right subarray is sorted
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1




s = Solution()

assert(s.search([4,5,6,7,0,1,2], 0) == 4)
assert(s.search([4,5,6,7,0,1,2], 3) == -1)
assert(s.search([1], 0) == -1)