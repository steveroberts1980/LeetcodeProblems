# https://leetcode.com/problems/multiply-strings/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # This can happen in 2 passes
        # First pass we multiply all the digits
        # Second pass, we add all the individual results until we are only left with a single result

        result = ''
        stack = []

        def add(num1: str, num2: str) -> str:
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

        for i in range(len(num1)):
            carry = 0
            n1 = num1[len(num1) - 1 - i]
            v1 = ord(n1) - ord('0')

            stack.extend(['0'] * i)

            for j in range(len(num2)):
                n2 = num2[len(num2) - 1 - j]
                v2 = ord(n2) - ord('0')

                tmp = carry + (v1 * v2)
                carry = tmp // 10
                tmp = tmp - (carry * 10)
                stack.append(chr(ord('0') + tmp))

            if carry:
                stack.append(chr(ord('0') + carry))
            tmp2 = ''
            while stack:
                val = stack.pop()

                if val == '0' and not tmp2:
                    continue
                tmp2 += val

            if result:
                result = add(result, tmp2)
            else:
                result = tmp2


        return result if result else "0"


s = Solution()

assert(s.multiply("408", "5") == "2040")
assert(s.multiply("9133", "0") == "0")
# assert(s.multiply("2", "3") == "6")
assert(s.multiply("123", "456") == "56088")

