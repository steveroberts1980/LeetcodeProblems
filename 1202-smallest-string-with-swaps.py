# https://leetcode.com/problems/smallest-string-with-swaps/

from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adjacent =  []

        for _ in range(len(s)):
            adjacent.append([])

        visited = [False] * len(s)
        s = [s[i] for i in range(len(s))]

        def DFS(s: str, vertex: int, characters: list, indices: list):
            # Add the character and index to the list
            characters.append(s[vertex])
            indices.append(vertex)

            visited[vertex] = True

            # Traverse the adjacents
            for adj in adjacent[vertex]:
                if not visited[adj]:
                    DFS(s, adj, characters, indices)

        for x, y in pairs:
            adjacent[x].append(y)
            adjacent[y].append(x)

        for i in range(len(s)):
            # if not covered in the DFS yet
            if not visited[i]:
                characters = list()
                indices = list()

                DFS(s, i, characters, indices)

                # Sort the list of characters and indices
                characters.sort()
                indices.sort()

                for j in range(len(characters)):
                    s[indices[j]] = characters[j]

        return ''.join(s)

s = Solution()

assert(s.smallestStringWithSwaps("dcab", [[0,3],[1,2]]) == "bacd")
assert(s.smallestStringWithSwaps("abcd", [[0,3],[1,2],[0,2]]) == "abcd")
assert(s.smallestStringWithSwaps("cba", [[0,1],[1,2]]) == "abc")



