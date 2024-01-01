# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in letters.keys():
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in letters.keys():
                letters[t[i]] -= 1

                if letters[t[i]] < 0:
                    return False
            else:
                return False
        
        sum = 0
        for v in letters.values():
            sum += v

        return sum == 0
    
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}

        for i in range(len(s)):
            letters[s[i]] = 1 + letters.get(s[i], 0)
            letters[t[i]] = letters.get(t[i], 0) - 1

        for l in letters:
            if letters[l] != 0:
                return False
        
        return True
    
# What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        s = s.lower()
        t = t.lower()

        for i in range(len(s)):
            letters[ord(s[i])-97] += 1
            letters[ord(t[i])-97] -= 1

        for i in range(len(letters)):
            if letters[i] != 0:
                return False

        return True
                         

s = Solution3()


#assert(s.isAnagram("anagram", "nagaram"))
assert(not s.isAnagram("rat", "car"))
