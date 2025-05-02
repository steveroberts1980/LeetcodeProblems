# https://leetcode.com/problems/goat-latin/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&status=TO_DO%2CATTEMPTED&difficulty=EASY

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        aCounter = 1
        result = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for s in sentence.split(' '):
            tmp = []

            if s[0] in vowels:
                tmp.append(s)
                tmp.append('ma')
            else:
                tmp.append(s[1:])
                tmp.append(s[0])
                tmp.append('ma')

            tmp.extend(['a']*aCounter)

            result.append("".join(tmp))

            aCounter += 1

        return " ".join(result)

s = Solution()

assert(s.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
assert(s.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
