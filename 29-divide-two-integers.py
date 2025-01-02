# https://leetcode.com/problems/divide-two-integers/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = pow(2, 31) - 1
        MIN_INT = - pow(2, 31)

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        if divisor == 1:
            return dividend
        
        if divisor == -1:
            return -dividend
        
        numNegatives = 0

        if dividend < 0:
            numNegatives += 1
        else:
            dividend = -dividend

        if divisor < 0:
            numNegatives += 1
        else:
            divisor = -divisor
        
        quotient = 0

        while dividend <= divisor:
            powerOfTwo = divisor
            tmpQuotient = 1

            while powerOfTwo < dividend and :
                powerOfTwo += powerOfTwo
                tmpQuotient += tmpQuotient

            quotient += tmpQuotient
            dividend -= powerOfTwo

        if numNegatives == 1:
            quotient = -quotient
            
        return quotient


s = Solution()

assert(s.divide(10, 3) == 3)
assert(s.divide(7, -3) == -2)
