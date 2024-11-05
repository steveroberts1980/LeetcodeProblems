# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack&status=TO_DO%2CATTEMPTED

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # brute force
        # Can do this recursively until the recursive function does not make a removal
        # Time limit was exceeded

        def remove_dups_helper(s: str) -> str:
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    return s[0:i] + s[i+2:]
                
            return s
                

        tmp = s

        while True:
            tmp = remove_dups_helper(s)

            if len(s) == len(tmp):
                break

            s = tmp
        
        return tmp

    # After the hint to use the stack, developed the following method
    def removeDuplicates(sefl, s: str) -> str:
        if not s:
            return ""
        
        result = list()

        # push the first character onto the stack.
        # check if the next character matches
        # if so, then discard the next and pop
        # the top off the stack.
        result.append(s[0])
        for i in range(1, len(s)):
            if len(result) and s[i] == result[-1]:
                result.pop()
            else:
                result.append(s[i])
        
        return "".join(result)

s = Solution()

assert(s.removeDuplicates("abbaca") == "ca")
assert(s.removeDuplicates("azxxzy") == "ay")
