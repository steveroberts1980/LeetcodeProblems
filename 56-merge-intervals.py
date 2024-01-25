# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals
        
        res = []
        
        intervals.sort(key = lambda i : i[0])

        j = 1
        current = intervals[0]

        while j < len(intervals):
            # If the start of the next interval is within the current interval
            # expand the current to the end of the greater of the 2.
            if intervals[j][0] <= current[1]:
                current[1] = max(intervals[j][1], current[1])
            else:
                res.append(current)
                current = intervals[j]

            j += 1
        
        # Add the last interval evaluated or updated
        res.append(current)
        return res


s = Solution()


#assert(s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])
assert(s.merge([[1,4],[4,5]]) == [[1,5]])

