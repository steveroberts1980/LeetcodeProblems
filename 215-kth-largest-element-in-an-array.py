# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO%2CATTEMPTED&role=full-stack

from typing import List
import heapq

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     h = []

    #     for n in nums:
    #         heapq.heappush(h, n)

    #     for i in range(0, len(nums) + 1 - k):
    #         val = heapq.heappop(h)

    #     return val
    
# After reading the solution, there is an optimization. I can keep the heap at size k and then at the end,
# return the first element popped.

    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for n in nums:
            heapq.heappush(h, n)
            
            if len(h) > k:
                heapq.heappop(h)

        return heapq.heappop(h)


s = Solution()


assert(s.findKthLargest([3,2,1,5,6,4], 2) == 5)
assert(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4)

