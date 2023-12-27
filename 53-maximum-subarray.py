from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = pow(10, 4)*(-1) - 1
        sum = 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                max_value = max(max_value, sum)

        return max_value        

class Solution_Kadane:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = pow(10, 4)*(-1) - 1
        sum = 0
        for i in range(len(nums)):
            sum = max(nums[i], sum + nums[i])
            max_value = max(max_value, sum)

        return max_value


s = Solution()
s = Solution_Kadane()

assert(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
assert(s.maxSubArray([1]) == 1)
assert(s.maxSubArray([5,4,-1,7,8]) == 23)

