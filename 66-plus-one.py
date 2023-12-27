# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        if digits[-1] == 9:
            carry = 1
            digits[-1] = 0
        else:
            digits[-1] = digits[-1] + 1

        if carry:
            for i in range(len(digits) - 1):
                if (digits[-2-i] == 9):
                    carry = 1
                    digits[-2-i] = 0
                else:
                    carry = 0
                    digits[-2-i] = digits[-2-i] + 1
                    break

        if carry:
            digits.insert(0, 1)

        return digits
    
s = Solution()

assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([9]) == [1,0]
assert s.plusOne([9,9,9]) == [1,0,0,0]
