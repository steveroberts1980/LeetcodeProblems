from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i + 1)
                print(comb)
                backtrack(remain - i - 1, comb, i + 1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results


s = Solution()

assert(s.combinationSum3(3, 7) == [[1,2,4]])
#assert(s.combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]])
#assert(s.combinationSum3(4, 1) == [])
