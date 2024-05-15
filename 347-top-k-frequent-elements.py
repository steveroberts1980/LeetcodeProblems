# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        count_array = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        for key, val in hash_map.items():
            count_array[val].append(key)

        ret_val = []

        for i in range(len(nums), 0, -1):
            while len(count_array[i]):
                ret_val.append(count_array[i].pop())
                if len(ret_val) == k:
                    return ret_val



s = Solution()

assert(s.topKFrequent([1,1,1,2,2,3], 2) == [1,2])
assert(s.topKFrequent([1], 1) == [1])
