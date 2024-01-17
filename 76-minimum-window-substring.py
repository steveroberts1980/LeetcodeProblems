# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def hashes_match(hash1, hash2):
            for k in list(hash1.keys()):
                if (k not in hash2.keys()) or (hash2[k] < hash1[k]):
                    return False
                
            return True

        #Start both pointers at 0. 
        l, found_chars = 0, 0
        hash, hashT = {}, {}
        sub_index = [-1, -1]

        # Initialize our hash
        for c in t:
            hashT[c] = hashT.get(c, 0) + 1

        total_chars = len(hashT.keys())

        # Run the right pointer from the start of the string to the end
        for r in range(len(s)):
            # If the character is a needed one
            c = s[r]
            hash[c] = hash.get(c, 0) + 1

            if c in hashT and hash[c] == hashT[c]:
                found_chars += 1

            while found_chars == total_chars:
                if (sub_index[0] == -1) or ((r - l) < sub_index[1] - sub_index[0]):
                    sub_index = [l, r]

                # Now start removing left characters
                hash[s[l]] -= 1
                if s[l] in hashT and hash[s[l]] < hashT[s[l]]:
                    found_chars -= 1
                l += 1
        
        if sub_index[0] == -1:
            return ""
        else:
            return s[sub_index[0]:sub_index[1]+1]

s = Solution()


assert(s.minWindow("ADOBECODEBANC", "ABC") == "BANC")
assert(s.minWindow("a", "a") == "a")
assert(s.minWindow("a", "aa") == "")

