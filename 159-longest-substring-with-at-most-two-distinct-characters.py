# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/?envType=problem-list-v2&envId=hash-table

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinctChars = 0
        chars = defaultdict(None)
        maxLength = -1

        # Use 2 pointers to simplify this
        left = right = 0

        while right < len(s):
            # do work here
            if not chars.get(s[right], 0):
                distinctChars += 1
            
            # Update the char count in the substring
            chars[s[right]] = chars.get(s[right], 0) + 1

            while distinctChars > 2:
                # move the left pointer and update values
                chars[s[left]] -= 1

                # Once we have eliminated one of the extra chars, 
                # update the count
                if not chars[s[left]]:
                    distinctChars -= 1

                left += 1

            maxLength = max(maxLength, right - left + 1)

            right += 1

        return maxLength


s = Solution()


assert(s.lengthOfLongestSubstringTwoDistinct("eceba") == 3)
assert(s.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5)