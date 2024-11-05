# https://leetcode.com/problems/range-sum-of-bst/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack&status=TO_DO%2CATTEMPTED

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node : TreeNode, low, high, sum):
            if node:
                if node.val >= low and node.val <= high:
                    sum += node.val

                if node.val >= low:    
                    sum = dfs(node.left, low, high, sum)
                
                if node.val <= high:
                    sum = dfs(node.right, low, high, sum)

            return sum


        return dfs(root, low, high, 0)


s = Solution()

root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))

assert(s.rangeSumBST(root, 7, 15) == 32)

root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))), TreeNode(15, TreeNode(13), TreeNode(18)))

assert(s.rangeSumBST(root, 6, 10) == 23)

