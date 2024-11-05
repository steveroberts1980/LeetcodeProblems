# https://leetcode.com/problems/asteroid-collision/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # This needs to be done by looking at the next number each time and comparing with the current
        # If the next number destroys the current, then we will need to compare with the previous
        # This tells me that a stack will be the best choice.
        # There will be a few cases:
        # current and stack.peek are both positive or negative, then push current onto the stack
        # abs(current) < stack.peek = remove current
        # abs(current) > stack.peek = pop stack and then check next peek until current is ready to push

        def peek(s: List[int]):
            if s:
                return s[len(s) - 1]
            else:
                return None
            
        if not asteroids:
            return []
        
        results = list()
        
        # push the first item onto the stack/queue
        results.append(asteroids[0])

        for i in range(1, len(asteroids)):
            store = True
            while peek(results):
                tmp = peek(results)
                if asteroids[i] * tmp > 0: # they are traveling in the same direction
                    break
                else:
                    if tmp < asteroids[i]: # They are travelling away from each other.
                        break
                    elif tmp + asteroids[i] == 0:
                        results.pop()
                        store = False
                        break
                    elif abs(tmp) < abs(asteroids[i]):
                        results.pop()
                    else:
                        store = False
                        break
                
            if store:
                results.append(asteroids[i])
        
        return results


s = Solution()

#assert(s.asteroidCollision([1,-2,-2,-2]) == [-2,-2,-2])
#assert(s.asteroidCollision([5,10,-5]) == [5,10])
assert(s.asteroidCollision([8,-8]) == [])
assert(s.asteroidCollision([10,2,-5]) == [10])