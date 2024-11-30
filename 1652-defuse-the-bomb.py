# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18


from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # will go with a sliding window approach since this will allow 
        # to only traverse once through.
        # In this approach, I will get the sum for the first element, 
        # then shift the window once to the right. When shifting, need to subtract
        # the left element and add the next right element.
        list_length = len(code)
        decoded = [0] * list_length
        start = 1
        if k < 0:
            start = list_length + k

        end = start
        sum = 0

        for i in range(abs(k)):
            sum += code[end % list_length]
            end += 1

        end -= 1

        for i in range(list_length):
            decoded[i] = sum

            sum -= code[start % list_length]
            start += 1
            end += 1
            sum += code[end % list_length]

        return decoded        

s = Solution()

assert(s.decrypt([5,7,1,4], 3) == [12,10,16,13])
assert(s.decrypt([1,2,3,4], 0) == [0,0,0,0])
assert(s.decrypt([2,4,9,3], -2) == [12,5,6,13])