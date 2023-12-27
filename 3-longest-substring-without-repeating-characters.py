#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
            
        longest = 1
        ptr1 = 0

        for i in range(1, len(s)):
            sub = s[ptr1 : i]
            longest = max(longest, len(sub))
            #print(sub)
            while sub.__contains__(s[i]) and ptr1 < i:
                ptr1 = ptr1 + 1
                sub = s[ptr1 : i]

        return longest
    

s = Solution()

print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))