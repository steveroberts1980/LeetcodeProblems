#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, left, right, sub = 0, 0, 0, ''

        for right in range(0, len(s)):
            while sub.__contains__(s[right]) and left < right:
                left = left + 1
                sub = s[left : right]

            sub = s[left : right + 1]

            longest = max(longest, len(sub))

        return longest
    

s = Solution()

assert(s.lengthOfLongestSubstring('') == 0)
assert(s.lengthOfLongestSubstring(' ') == 1)
assert(s.lengthOfLongestSubstring("au") == 2)
assert(s.lengthOfLongestSubstring("abcabcbb") == 3)
assert(s.lengthOfLongestSubstring("bbbbb") == 1)
assert(s.lengthOfLongestSubstring("pwwkew") == 3)