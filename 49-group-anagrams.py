# https://leetcode.com/problems/group-anagrams/

from typing import List, DefaultDict

# My solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retVal = []

        for word in strs:
            found = False
            for groupings in retVal:
                if len(groupings[0]) > 0 and len(groupings[0]) == len(word):
                    checkWord = str(groupings[0])
                    for i in range(len(word)):
                        checkWord = checkWord.replace(word[i], '', 1)
                    
                    if checkWord == "":
                        found = True
                        groupings.insert(0, word)
                elif groupings[0] == word:
                    found = True
                    groupings.insert(0, word)
                    
            if not found:
                retVal.insert(0, [word])

        return retVal

# After watching the neetcode explanation but before their code solution
# https://www.youtube.com/watch?v=vzdNOK2oB2E
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            hashVal = [0] * 26

            for i in range(len(word)):
                hashVal[ord(word[i]) - ord('a')] += 1

            hashVal = tuple(hashVal)
            anagramList = anagramMap.get(hashVal, [])
            anagramList.insert(0, word)
            anagramMap[hashVal] = anagramList

        return list(anagramMap.values())
    
# Neetcode solution
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = DefaultDict(list)

        for word in strs:
            hashVal = [0] * 26

            for i in range(len(word)):
                hashVal[ord(word[i]) - ord('a')] += 1

            anagramMap[tuple(hashVal)].append(word)

        return list(anagramMap.values())    

s = Solution2()



print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]))
#print(s.groupAnagrams(["","b"]))
#print(s.groupAnagrams(["",""]))
exit()

assert(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]])
assert(s.groupAnagrams([""]) == [[""]])
assert(s.groupAnagrams(["a"]) == [["a"]])

