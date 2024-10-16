# https://leetcode.com/problems/valid-word-abbreviation/submissions/1421459331/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # ordinal 0 starts at 48
        # if ordinal char > 47, then it is a number.
        # Number value is ord('number') - ord('0')
        word_ptr = 0
        abbr_ptr = 0

        while abbr_ptr < len(abbr) and word_ptr < len(word):
            tmpNum = ""
            if not abbr[abbr_ptr].isdigit():
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                
                word_ptr += 1
                abbr_ptr += 1
            else:
                if abbr[abbr_ptr] == '0':
                    return False
                
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    tmpNum += abbr[abbr_ptr]
                    abbr_ptr += 1

                word_ptr += int(tmpNum)

        return abbr_ptr == len(abbr) and word_ptr == len(word)


s = Solution()

assert(s.validWordAbbreviation("internationalization", "i12iz4n"))
assert(not s.validWordAbbreviation("apple", "a2e"))
assert(s.validWordAbbreviation("internationalization", "i5a11o1"))
assert(not s.validWordAbbreviation("substitution", "s55n"))
assert(not s.validWordAbbreviation("substitution", "s010n"))
assert(not s.validWordAbbreviation("substitution", "s0ubstitution"))
assert(not s.validWordAbbreviation("a", "2"))
assert(not s.validWordAbbreviation("hi", "h2"))
assert(not s.validWordAbbreviation("word", "3e"))
