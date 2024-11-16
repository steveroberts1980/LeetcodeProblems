# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

######################################
# Heap Sort
######################################

from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate distance
        # Check if distance is less than current greatest
        # Push tuple of distance and point onto heap
        # pop k elements off the heap
        # return
        closest = []
        heap = []

        def distance(x: int, y: int) -> float:
            return math.sqrt(pow(x, 2) + pow(y, 2))

        for x,y in points:
            heapq.heappush(heap, (distance(x, y), [x, y]))

        for i in range(k):
            _, point = heapq.heappop(heap)

            closest.append(point)    

        return closest


s = Solution()

assert(s.kClosest([[1,3],[-2,2]], 1) == [[-2,2]])
assert(s.kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]])