# https://leetcode.com/problems/majority-element-ii/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_threshold = len(nums) // 3
        occurences = defaultdict(int)
        elements = []

        for n in nums:
            occurences[n] += 1
        
        for k in occurences:
            if occurences[k] > majority_threshold:
                elements.append(k)

        return elements
    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        majority_threshold = len(nums) // 3
        elements = []

        nums.sort()
        current = nums[0]
        counter = 0

        for n in nums:
            if n == current:
                counter += 1
            else:
                if counter > majority_threshold:
                    elements.append(current)
                current = n
                counter = 1

        if counter > majority_threshold:
            elements.append(current)
        
        return elements
    



s = Solution()

assert(s.majorityElement([3, 2, 3]) == [3])
assert(s.majorityElement([1]) == [1])
assert(s.majorityElement([1,2]) == [1,2])
