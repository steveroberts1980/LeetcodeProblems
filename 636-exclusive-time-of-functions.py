# https://leetcode.com/problems/exclusive-time-of-functions/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        execution_times = [0] * n
        execution_stack = []
        prev_start_time = 0

        for e in logs:
            id, state, time = e.split(':')
            id = int(id)
            time = int(time)
            
            if state == "start":
                # if there is already a process on the stack,
                if execution_stack:
                    execution_times[execution_stack[-1]] += time - prev_start_time
                # pop it and update its execution time
                execution_stack.append(id)
                prev_start_time = time
            else: # process is ending
                execution_times[execution_stack.pop()] += time - prev_start_time + 1
                prev_start_time = time + 1

        return execution_times



s = Solution()

assert(s.exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]) == [3,4])
assert(s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]) == [8])
assert(s.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]) == [7,1])