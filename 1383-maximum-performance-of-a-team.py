# https://leetcode.com/problems/maximum-performance-of-a-team/

from typing import List
import heapq
#from collections import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        performance = 0
        totalSpeed = 0
        speedHeap = []
        engineers = []
        
        # First, sort the values. We will sort by efficiencies and then start evaluating based on efficiencies
        # from greatest to least. Once we start evaluating lower efficiencies, the previous efficiencies don't matter.
        # Only the engineer's speeds matter that point.
        # We can use a min heap to remove the slower engineers once we have k values in the heap.

        for i in range(len(speed)):
            engineers.append([efficiency[i], speed[i]])

        engineers.sort(reverse=True)

        for e in engineers:
            # Keep track of the total speed
            if len(speedHeap) == k:
                totalSpeed -= heapq.heappop(speedHeap)

            totalSpeed += e[1]
            heapq.heappush(speedHeap, e[1])

            performance = max(performance, totalSpeed * e[0])

        return performance % (pow(10, 9) + 7)


s = Solution()


speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]

assert(s.maxPerformance(6, speed, efficiency, 2) == 60)

speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]

assert(s.maxPerformance(6, speed, efficiency, 3) == 68)

speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]

assert(s.maxPerformance(6, speed, efficiency, 4) == 72)

