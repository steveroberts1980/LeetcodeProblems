# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&status=TO_DO&difficulty=MEDIUM&role=backend

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}

        for i in range(len(nums)):
            if nums[i]:
                self.vector[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for k, v in self.vector.items():
            if k in vec.vector:
                product += v * vec.vector[k]

        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert(v1.dotProduct(v2) == 8)

nums1 = [0,1,0,0,0]
nums2 = [0,0,0,0,2]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert(v1.dotProduct(v2) == 0)

nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert(v1.dotProduct(v2) == 6)


nums1 = [0,0,0,0,0,0,3,0,0,3,0,0,0]
nums2 = [0,0,2,0,0,4,3,0,0,2,0,0,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert(v1.dotProduct(v2) == 15)