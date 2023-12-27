# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr1 = l = ret = 0

        while ptr1 < len(s):
            if s[ptr1] == ' ':
                l = 0
            else:
                l += 1
                ret = l
            
            ptr1 += 1

        return ret

s = Solution()

assert s.lengthOfLastWord("Hello World") == 5
assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
assert s.lengthOfLastWord("luffy is still joyboy") == 6
