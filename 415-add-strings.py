# https://leetcode.com/problems/add-strings/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY



class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
            carry = 0
            ptr1 = len(num1) - 1
            ptr2 = len(num2) - 1
            result = []

            # while the pointers are not at the end of the strings
            # get the ordinal offsets and add the 2
            # if the value is greater than 9, mod by 10 to get the remainer
            # then the carry is val - remainder / 10

            while ptr1 >= 0 or ptr2 >= 0:
                v1 = ord(num1[ptr1]) - ord('0') if ptr1 >= 0 else 0
                v2 = ord(num2[ptr2]) - ord('0') if ptr2 >= 0 else 0

                tmp = v1 + v2 + carry
                rem = tmp % 10
                carry = (tmp - rem) // 10

                result.append(chr(ord('0') + rem))

                ptr1 -= 1
                ptr2 -= 1

            if carry:
                 result.append(chr(ord('0') + carry))

            # Now reverse the digits
            result.reverse()

            # Join the individual digits to a single string an return
            return "".join(result)


    

s = Solution()

assert(s.addStrings("11", "123") == "134")
assert(s.addStrings("456", "77") == "533")
assert(s.addStrings("0", "0") == "0")

