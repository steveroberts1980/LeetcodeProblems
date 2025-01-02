# https://leetcode.com/problems/two-sum-iii-data-structure-design/?envType=problem-list-v2&envId=hash-table

from collections import defaultdict

class TwoSum:
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        self.nums[number] = self.nums.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for n in self.nums:
            diff = value - n

            if diff == n and self.nums[n] > 1:
                return True
            elif diff != n and diff in self.nums:
                return True
            
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

