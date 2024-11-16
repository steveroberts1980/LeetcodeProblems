# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&status=TO_DO&difficulty=MEDIUM&role=backend

from typing import Optional

######################################
# Binary Tree DFS
######################################


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        # Use DFS
        # At the leaf node, add the total to the global total value
        # Each recursive call, take the current total and multiply by 10 then add current node val

        def dfs(node, cur_sum):
            nonlocal total
            cur_sum = cur_sum * 10 + node.val

            if not node.left and not node.right:
                total += cur_sum

            if node.left:
                dfs(node.left, cur_sum)

            if node.right:
                dfs(node.right, cur_sum)

        dfs(root, 0)
        return total

s = Solution()

root = TreeNode(1, TreeNode(2), TreeNode(3))

assert(s.sumNumbers(root) == 25)

root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
