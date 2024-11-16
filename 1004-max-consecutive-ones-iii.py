# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

######################################
# Sliding Window
######################################

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Using 2 pointers
        # While we have 0s to flip, keep increasing the distance between the 2 pointers
        # When we run out of 0s and hit another, we need to move the left until we get 
        # more 0s to flip and then keep moving the right pointer
        # Go until the right pointer hits the end.
        if not nums:
            return 0

        longest = 0
        left = right = 0
        remaining_flips = k

        for right in range(len(nums)):
            if not nums[right]:
                remaining_flips -= 1
            
            # Now need to move in the left side until we unflip again
            while left <= right and remaining_flips < 0:
                if not nums[left]:
                    remaining_flips += 1

                left += 1

            longest = max(longest, right - left + 1)

        return longest



s = Solution()

assert(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6)
assert(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10)