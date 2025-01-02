# https://leetcode.com/problems/shortest-word-distance-ii/?envType=problem-list-v2&envId=hash-table

from typing import List
from collections import defaultdict

class WordDistance:
    words = defaultdict(list)

    def __init__(self, wordsDict: List[str]):
        for i in range(len(wordsDict)):
            self.words[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        shortest = 3 * pow(10, 4) + 1

        for i in self.words[word1]:
            for j in self.words[word2]:
                shortest = min(shortest, abs(i - j))

        return shortest


s = WordDistance(["a","a","b","b"])
assert(s.shortest("a", "b") == 1)
assert(s.shortest("b", "a") == 1)

s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
assert(s.shortest("coding", "practice") == 3)
assert(s.shortest("makes", "coding") == 1)


