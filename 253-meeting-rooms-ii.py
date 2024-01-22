# https://leetcode.com/problems/meeting-rooms-ii/description/

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms = 0
        current_rooms = 0

        start_times, end_times = [], []
        for m in intervals:
            start_times.append(m[0])
            end_times.append(m[1])

        start_times.sort()
        end_times.sort()
        i = j = 0

        while i < len(start_times):
            if start_times[i] < end_times[j]:
                current_rooms += 1
                max_rooms = max(max_rooms, current_rooms)
                i += 1
            else:
                current_rooms -= 1
                j += 1

        return max_rooms


s = Solution()

assert(s.minMeetingRooms([[0,30],[5,10],[15,20]]) == 2)
assert(s.minMeetingRooms([[7,10],[2,4]]) == 1)

