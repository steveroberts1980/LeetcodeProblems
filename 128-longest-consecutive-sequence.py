from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0

        for num in nums:
            if (num - 1) in num_set: # Don't check numbers that have already been checked as part of a longer secquence.
                continue # There is a smaller number already in the set, so we want to start checking our sequence with that.

            cur_seq = 1

            while (num + 1 in num_set):
                cur_seq += 1
                num += 1

            max_sequence = max(max_sequence, cur_seq)

        return max_sequence

s = Solution()

assert(s.longestConsecutive([100,4,200,1,3,2]) == 4)
assert(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9)

