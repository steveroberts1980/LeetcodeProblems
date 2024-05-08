from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        combos = [amount + 1] * (amount + 1)
        combos[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    combos[a] = min(combos[a], 1 + combos[a -c])

        return combos[amount] if combos[amount] < amount + 1 else -1

s = Solution()

assert(s.coinChange([1,2,5], 11) == 3)
assert(s.coinChange([2], 3) == -1)
assert(s.coinChange([1], 0) == 0)