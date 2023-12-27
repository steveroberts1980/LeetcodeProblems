from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowPrice = pow(10, 5) + 1

        for i in range(len(prices)):
            if prices[i] < lowPrice:
                lowPrice = prices[i]
            elif prices[i] - lowPrice > maxProfit:
                maxProfit = prices[i] - lowPrice

        return maxProfit

s = Solution()

assert(s.maxProfit([7,1,5,3,6,4]) == 5)
assert(s.maxProfit([7,6,4,3,1]) == 0)
