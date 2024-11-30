# https://leetcode.com/problems/random-pick-index/

from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.values = {}

        for i in range(len(nums)):
            indexes = self.values.get(nums[i], [])
            indexes.append(i)
            self.values[nums[i]] = indexes

    def pick(self, target: int) -> int:
        indexes = self.values[target]

        return random.choice(indexes)
    
