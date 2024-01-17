# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # I am going to take the same approach as finding all the palindroming substrings. #647
        # Just keep track of the max substring

        retVal = ''

        for i in range(len(s)):
            # First check all the odd length substrings
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(retVal):
                    retVal = s[left:right+1]

                left -= 1
                right += 1

            # Now check the even length substrings
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(retVal):
                    retVal = s[left:right+1]

                left -= 1
                right += 1

        return retVal

s = Solution()

assert(s.longestPalindrome("babad") == "bab")
assert(s.longestPalindrome("cbbd") == "bb")

