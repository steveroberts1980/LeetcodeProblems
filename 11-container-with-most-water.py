from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxArea = max(maxArea, (j-i) * (min(height[i], height[j])))

        return maxArea

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0

        def area(x, y):
            return (y - x) * min(height[x], height[y])
        
        while i < j:
            maxArea = max(maxArea, area(i, j))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return maxArea

s = Solution2()

assert(s.maxArea([1,2,3,4,5,25,24,3,4]) == 24)
assert(s.maxArea([1,3,2,5,25,24,5]) == 24)
assert(s.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
assert(s.maxArea([1,1]) == 1)