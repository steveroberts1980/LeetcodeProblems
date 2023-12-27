from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retVal = []
        # Sort the array first
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans = [nums[i], nums[j], nums[k]]

                    if ans not in retVal:
                        retVal.append(ans)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return retVal

s = Solution()

assert(s.threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]])
#assert(s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
#assert(s.threeSum([0,1,1]) == [])
#assert(s.threeSum([0,0,0]) == [[0,0,0]])