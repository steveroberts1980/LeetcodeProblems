# https://leetcode.com/problems/missing-ranges/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack

######################################
# Two pointers
######################################

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # Brute force would be to run through the range from lower to upper and everytime we hit 
        # a value in the given list, record the latest range up to that number

        # Or, we can start with our lower bound at lower and then pick the first number
        # in the nums list. Select that number - 1 as the upper bound. If the upper 
        # bound >= lower bound, record that as a range

        # Do that until the end of the input array is reached. If the last number is 
        # less than upper, ensure the final range is captured.

        ranges = list()

        for i in range(len(nums)):
            tmp_upper = nums[i] -1

            if tmp_upper >= lower:
                ranges.append([lower, tmp_upper])

            lower = nums[i] + 1

        if upper >= lower:
            ranges.append([lower, upper])

        return ranges


s = Solution()

assert(s.findMissingRanges([0,1,3,50,75], 0, 99) == [[2,2], [4,49], [51,74], [76, 99]])
assert(s.findMissingRanges([-1], -1, -1) == [])

