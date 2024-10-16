# https://leetcode.com/problems/valid-palindrome-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Start with a left and right pointer
        # while left <= right, continue as long as they are equal
        # If they are not equal, check the left+1 or right-1

        def valid(s: str, canDelete=True) -> bool:
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                elif canDelete:
                    # Now check if substring is a valid palindrome
                    return valid(s[(left + 1):(right + 1)], False) or valid(s[left:right], False)
                else:
                    return False
                
            return True
        
        return valid(s)

s = Solution()

assert(s.validPalindrome("aba"))
assert(s.validPalindrome("abca"))
assert(not s.validPalindrome("abc"))
assert(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))

#cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu