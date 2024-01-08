# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

# Not constant memory space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tmp = [0] * len(nums)
        for i in range(0, len(nums)):
            if tmp[nums[i] - 1] > 0:
                return nums[i]
            
            tmp[nums[i] - 1] = 1

        return -1

# Using Floyd's Algorithm
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        # First, need to view as a linked list.
        # Then traverse the list with a slow and fast pointer.
        # Once the intersection is found in the cycle, start another pointer from the start and move it along with the slow pointer.
        # Where those 2 meet is the start of the cycle and will be the repeated number.
        # 
        #  0  1  2  3  4 
        # [1, 3, 4, 2, 2]

        slow, fast = 0, 0

        for i in range(len(nums)):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
        
        new_slow = 0
        for i in range(len(nums)):
            new_slow = nums[new_slow]
            slow = nums[slow]

            if slow == new_slow:
                print(f'slow={slow}, fast={new_slow}')
                return  slow


s = Solution2()

assert(s.findDuplicate([1,3,4,2,2]) == 2)
assert(s.findDuplicate([3,1,3,4,2]) == 3)