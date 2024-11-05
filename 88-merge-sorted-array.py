# https://leetcode.com/problems/merge-sorted-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Starting at the beginning of each array an merging will require
        # a lot of shifting of the array elements.
        # If we start at the end of each array and work towards the start
        # then we can save the shifting and only run through each array
        # one time

        l1_ptr = m - 1
        l2_ptr = n - 1
        end_ptr = m + n -1

        while end_ptr >= 0 and l1_ptr >= 0 and l2_ptr >= 0:
            if nums1[l1_ptr] > nums2[l2_ptr]:
                nums1[end_ptr] = nums1[l1_ptr]
                end_ptr -= 1
                l1_ptr -= 1
            else:
                nums1[end_ptr] = nums2[l2_ptr]
                end_ptr -= 1
                l2_ptr -= 1
        
        if l2_ptr >= 0: # Finishing copying the remaining elements from the 2nd list
            while l2_ptr >= 0:
                nums1[end_ptr] = nums2[l2_ptr]
                end_ptr -= 1
                l2_ptr -= 1
        
        return



s = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

s.merge(nums1, 3, nums2, 3)

assert(nums1 == [1,2,2,3,5,6])

