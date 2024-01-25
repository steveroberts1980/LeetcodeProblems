# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Sort the list. Then add intervals to a result list
        # If an overlapping interval is found, don't add it to the result list.
        # Get the difference between the original list and the result list.

        # Sort by the first value in the interval then by the second value.
        # This will ensure we get the smaller intervals so we are eliminating the large
        # intervals if necessary which would not minimize the removed intervals.
        intervals.sort(key=lambda a: a[0]) #, a[1]))

        print(intervals)

        res = []

        res.append(intervals[0])

        for i in intervals[1:]:
            if i[0] >= res[-1][1]:
                res.append(i)
            elif i[1] < res[-1][1]:
                res.pop()
                res.append(i)

        print(len(intervals) - len(res))
        return len(intervals) - len(res)

s = Solution()

assert(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]) == 7)

assert(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1)
assert(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2)
assert(s.eraseOverlapIntervals([[1,2],[2,3]]) == 0)
