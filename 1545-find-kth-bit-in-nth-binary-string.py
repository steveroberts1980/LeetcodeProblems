# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY


class Solution2:
    # This is the solution from Leetcode
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: for S1, return '0'
        if n == 1:
            return "0"

        # Calculate the length of Sn
        length = 1 << n  # Equivalent to 2^n

        # If k is in the first half of the string, recurse with n-1
        if k < length // 2:
            return self.findKthBit(n - 1, k)

        # If k is exactly in the middle, return '1'
        elif k == length // 2:
            return "1"

        # If k is in the second half of the string
        else:
            # Find the corresponding bit in the first half and invert it
            corresponding_bit = self.findKthBit(n - 1, length - k)
            return "1" if corresponding_bit == "0" else "0"

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Brute force method. This will take 2^n time complexity and space complexity since the string 
        # doubles on each iteration.
        returnString = "0"

        def reverseAndInvert(s) -> str:
            newString = []
            charCount = len(s)

            for i in range(charCount):
                idx = charCount - 1 - i
                newString.append("0" if s[idx] == "1" else "1")

            return "".join(newString)


        for _ in range(n):
            returnString = "".join([returnString, "1", reverseAndInvert(returnString)])

        return returnString[k-1]

s = Solution()

assert(s.findKthBit(3, 1) == "0")
assert(s.findKthBit(4, 11) == "1")
