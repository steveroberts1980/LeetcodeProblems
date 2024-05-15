# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        # Multiply by -1 to implement a max heap
        heapq.heappush(self.max_heap, -1 * num)

        if (self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0]):
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)            

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return ((self.max_heap[0] * -1) + self.min_heap[0]) / 2.0 # return the avg of largest from max_heap and smallest from min_heap

mf = MedianFinder()

mf.addNum(1)
mf.addNum(2)
assert(mf.findMedian() == 1.5)
mf.addNum(3)
assert(mf.findMedian() == 2.0)
