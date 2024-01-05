# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stripped = ""
        tmp = []

        for i in range(len(s)):
            if str(s[i]).isalnum():
                stripped += s[i]

        if len(stripped) < 2:
            return True

        half_length = int(len(stripped) / 2)
        for i in range(half_length):
            tmp.append(stripped[i])

        skip = len(stripped) - 2*half_length
        for i in range(half_length + skip, len(stripped)):
            if tmp.pop() != stripped[i]:
                return False
        
        return True

# Another solution is to use 2 pointers, one at the start and one at the end and compare while left < right.
# Can check if is digit or alpha by comparing ord(char) for the ranges for number and character.


s = Solution()

assert(s.isPalindrome("a ba"))
assert(s.isPalindrome("A man, a plan, a canal: Panama"))
assert(not s.isPalindrome("race a car"))
assert(s.isPalindrome(" "))
