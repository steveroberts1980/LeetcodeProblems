# https://leetcode.com/problems/evaluate-division/

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        result = []

        def dfs(graph, start, end, visited) -> float:
            for variable, value in graph[start]:
                if variable in visited:
                    return 1.0
                
                visited.add(variable)
                if variable == end:
                    return value
                else:
                    return value * dfs(graph, variable, end, visited)
            visited.remove(start)

        # First, build the graph of bidirectional vertices and edges
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0 / values[i]))

        # Now, go through the queries one at a time and append the result
        for query in queries:
            # If either of the values are not in the graph, just append -1 to the result and move on
            if query[0] not in graph or query[1] not in graph:
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1.0)
            else:
                visited = set()
                result.append(dfs(graph, query[0], query[1], visited))

        return result



s = Solution()

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(s.calcEquation(equations, values, queries))

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(s.calcEquation(equations, values, queries))

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(s.calcEquation(equations, values, queries))