# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        number_mapping = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def get_combos(digits: str, combos: List[str]) -> List[str]:
            if not digits:
                return combos
            
            tmp = []
            
            for c in combos:
                for l in number_mapping[digits[0]]:
                    tmp.append(c + l)

            return get_combos(digits[1:], tmp)

        return get_combos(digits[1:], number_mapping[digits[0]])


s = Solution()

assert(s.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
assert(s.letterCombinations("") == [])
assert(s.letterCombinations("2") == ["a","b","c"])