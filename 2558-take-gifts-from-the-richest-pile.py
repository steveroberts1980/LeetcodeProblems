# https://leetcode.com/problems/take-gifts-from-the-richest-pile/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        giftHeap = []

        for gift in gifts:
            heapq.heappush(giftHeap, -1 * gift)

        for _ in range(k):
            tmp = -1 * heapq.heappop(giftHeap)
            tmp = -1 * (math.floor(math.sqrt(tmp)))

            heapq.heappush(giftHeap, tmp)

        remaining = 0
        while giftHeap:
            remaining += (heapq.heappop(giftHeap) * -1)

        return remaining

s = Solution()

gifts = [25,64,9,4,100]
k = 4

assert(s.pickGifts(gifts, k) == 29)

gifts = [1,1,1,1]
k = 4

assert(s.pickGifts(gifts, k) == 4)
