# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Sliding window. Start at all the way left.
        # Keep a hashmap of letter occurrences in the current window of the string.
        # length of substring - most occurring letter <= k means it is valid. Record as max if greater than previous max.
        # If length of substring - most occurring letter > k, need to slide the left pointer over 1 to the right.
        # Otherwise, keep sliding the right pointer over.
        # If length of entire string - i < max, then return. The result can't become greater.

        occurrences = [0] * 26
        retVal = 0
        i, j = 0, 0

        character_offset = ord('A')

        for j in range(len(s)):
            occurrences[ord(s[j]) - character_offset] += 1

            # find most occurring letter
            max_letter = 0
            for frequency in occurrences:
                max_letter = max(max_letter, frequency)

            while (j - i + 1) - max_letter > k:
                occurrences[ord(s[i]) - character_offset] -= 1
                i += 1


            retVal = max(retVal, j - i + 1)

        return retVal

s = Solution()

assert(s.characterReplacement("ABAB", 2) == 4)
assert(s.characterReplacement("AABABBA", 1) == 4)