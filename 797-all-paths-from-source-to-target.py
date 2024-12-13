# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        stack = []
        results = []

        stack.append([0])

        # Then, iteratively DFS to find all paths
        while stack:
            cur_path = stack.pop()

            for i in graph[cur_path[-1]]:
                new_path = cur_path.copy()
                new_path.append(i)

                if i == target:
                    results.append(new_path)
                else:
                    stack.append(new_path)

        return results

s = Solution()

graph = [[1,2],[3],[3],[]]
print(s.allPathsSourceTarget(graph))

graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(s.allPathsSourceTarget(graph))
