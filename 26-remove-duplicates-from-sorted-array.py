# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[k]:
                continue
            else:
                nums[k+1] = nums[i]
                k = k+1
        
        return k+1
    
s = Solution()
    
assert(s.removeDuplicates([1,1,2]) == 2)
assert(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5)