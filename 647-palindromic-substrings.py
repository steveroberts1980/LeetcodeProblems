# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Use two pointers. For each substring from start to end pointer,
        # check if palindrome
        # Slide window right. Continue to end and then widen window until width = len(s)

        # Each character is a palindrome, so initialize the counter here.
        counter = len(s)

        def isPalindrome(sub):
            i, j = 0, len(sub) - 1

            while i < j:
                if sub[i] != sub[j]:
                    return False
                
                i += 1
                j -= 1
                
            return True

        for window in range(1, len(s)):
            i, j = 0, window

            for _ in range(0, len(s) - j):
                counter = counter + int(isPalindrome(s[i:j+1]))
                i, j = i + 1, j + 1
        
        return counter
    
    # After watching the neetcode solution, giving a shot at coding up the explanation.
    # Find the odd palidromes and find the even palindromes.
class Solution2:
    def countSubstrings(self, s: str) -> int:

        count = 0

        # First get the odd length strings
        for i in range(len(s)):
            l = r = i # Start each set of pointers at the same spot.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        # Now get the even length strings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

s = Solution2()

assert(s.countSubstrings("abc") == 3)
assert(s.countSubstrings("aaa") == 6)
assert(s.countSubstrings("") == 0)


