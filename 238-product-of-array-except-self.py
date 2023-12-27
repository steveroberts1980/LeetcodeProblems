from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numElements = len(nums)
        retVal = []
        left = [1] * numElements
        right = [1] * numElements

        for i in range(numElements):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = left[i-1] * nums[i]

        for i in range(numElements):
            if i == 0:
                right[numElements - i - 1] = nums[numElements -  i - 1]
            else:
                right[numElements -i - 1] = right[numElements - i] * nums[numElements -  i - 1]

        for i in range(numElements):
            if i == 0:
                retVal.append(right[i + 1])
            elif i == numElements - 1:
                retVal.append(left[i - 1])
            else:
                retVal.append(left[i-1] * right[i+1])

        return retVal


s = Solution()

assert(s.productExceptSelf([1,2,3,4]) == [24,12,8,6])
assert(s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])

