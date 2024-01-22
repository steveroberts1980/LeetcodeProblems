# https://leetcode.com/problems/encode-and-decode-strings/description/

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        retVal = ""

        # To encode, we will first store the count of the number of characters in the string.
        # Then end that with a period.
        # Now it does not matter if the string contains a period or a number, we know how many 
        # characters make up that string and then we will be at the count for the next string.
        for s in strs:
            retVal += f'{len(s)}.{s}'

        return retVal

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        retVal = []
        while s:
            wordLength, s = s.split('.', 1)
            wordLength = int(wordLength)

            retVal.append(s[0:wordLength])
            s = s[wordLength:]                          

        return retVal



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
    
dummy_input = ["Hello","World"]

codec = Codec()

encoded = codec.encode(dummy_input)
print(codec.decode(encoded))

exit()

assert(codec.decode(codec.encode(dummy_input)) == dummy_input)

dummy_input = [""]

assert(codec.decode(codec.encode(dummy_input)) == dummy_input)
