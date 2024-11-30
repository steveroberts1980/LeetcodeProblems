# https://leetcode.com/problems/happy-number/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        num_str = str(n)

        while True:
            new_result = 0
            # Do work here. 
            for c in num_str:
                tmp = int(c)
                new_result += tmp * tmp 

            # Once the new_result is found, add it to the set
            # If the value already exists in the set, return False as this will start a cycle over.
            if new_result == 1:
                return True
            
            if new_result in nums:
                return False
            
            nums.add(new_result)
            num_str = str(new_result)


s = Solution()

assert(s.isHappy(19))
assert(not s.isHappy(2))
