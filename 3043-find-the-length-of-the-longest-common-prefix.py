# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 10

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        len = 0

        for digit in num_str:
            idx = int(digit)
            if node.children[idx]:
                len += 1
                node = node.children[idx]
            else:
                break
        return len

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        longest = 0

        for num in arr1:
            t.insert(num)

        for num in arr2:
            longest = max(longest, t.find_longest_prefix(num))

        return longest


s = Solution()

assert(s.longestCommonPrefix([1,10,100], [1000]) == 3)
assert(s.longestCommonPrefix([1,2,3], [4,4,4]) == 0)
