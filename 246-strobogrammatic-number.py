# https://leetcode.com/problems/strobogrammatic-number/?envType=problem-list-v2&envId=hash-table


class Solution:
    pairs = {
        "6":"9",
        "9":"6",
        "1":"1",
        "8":"8",
        "0":"0"
    }

    def isStrobogrammatic(self, num: str) -> bool:
        
        while len(num) > 1:
            if num[0] not in self.pairs:
                return False
            elif self.pairs[num[0]] != num[-1]:
                return False
            else:
                num = num[1:-1]

        return len(num) == 0 or num in ["1", "8"]



s = Solution()

assert(s.isStrobogrammatic("69"))
assert(s.isStrobogrammatic("88"))
assert(not s.isStrobogrammatic("962"))
assert(s.isStrobogrammatic("1"))
assert(s.isStrobogrammatic("11"))
assert(s.isStrobogrammatic("818"))
