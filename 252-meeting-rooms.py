# https://leetcode.com/problems/meeting-rooms/

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Need to check to see if any of the intervals overlap
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
             if intervals[i-1][1] > intervals[i][0]:
                  return False
            
        return True


s = Solution()

assert(s.canAttendMeetings([[13,15],[1,13]]))
assert(not s.canAttendMeetings([[0,30],[5,10],[15,20]]))
assert(s.canAttendMeetings([[7,10],[2,4]]))