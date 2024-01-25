# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])

        res = []
        tmp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= tmp[1]: # Intervals are overlapping
                tmp = [tmp[0], max(tmp[1], intervals[i][1])]
            else:
                res.append(tmp)
                tmp = intervals[i]
               
        res.append(tmp)
        return res


s = Solution()


assert(s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])
assert(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]])
