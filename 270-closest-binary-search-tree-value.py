# https://leetcode.com/problems/closest-binary-search-tree-value/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        cur_node = root
        closest = - -1000000

        while cur_node:
            if abs(cur_node.val - target) == abs(closest - target):
                closest = min(cur_node.val, closest)
            elif abs(cur_node.val - target) < abs(closest - target):
                closest = cur_node.val

            if cur_node.val == target:
                return cur_node.val
            elif cur_node.val < target:
                # go to the right and check
                cur_node = cur_node.right
            else: # cur_node.val > target
                # go to the left and check
                cur_node = cur_node.left

        return closest


s = Solution()

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

assert(s.closestValue(root, 3.5) == 3)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

assert(s.closestValue(root, 3.714286) == 4)

root = TreeNode(1)

assert(s.closestValue(root, 4.428571) == 1)