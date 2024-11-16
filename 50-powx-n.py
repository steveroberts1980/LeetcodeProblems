# https://leetcode.com/problems/powx-n/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

# Binary

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return_value = 1
        powers = {}
        keys= []
        invert = (n < 0)
        n = abs(n)
        # powers can be stored and referenced later
        # powers are added by multiplying their values i.e. (2^2)*(2^2) = 2^(2+2) = 2^4
        # 
        keys.append(1)
        exp = 2
        powers[1] = x
        while exp <= n:
            lookup = exp / 2
            powers[exp] = powers[lookup] * powers[lookup]
            keys.append(exp)
            exp = exp * 2
        
        keys.reverse()
        for i in keys:
            if i <= n:
                return_value = return_value * powers[i]
                n = n - i

        return 1.0 / return_value if invert else return_value


s = Solution()

print(s.myPow(200, 0))
#assert(s.myPow(2.0000, 10) == 1024.0)
#assert(s.myPow(2.1, 3) == 9.261)
#assert(s.myPow(2.0, -2) == 0.25)
