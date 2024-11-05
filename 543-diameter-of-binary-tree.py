# https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # The length is going to be the depth of the left side + the depth of the right side
    # We can do this by keeping track of the max depth with a dfs
        diameter = 0

        def dfs(root: TreeNode):
            if not root:
                return 0
            
            nonlocal diameter
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            diameter = max(diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        dfs(root)

        return diameter


s = Solution()

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

assert(s.diameterOfBinaryTree(root) == 3)

root = TreeNode(1, TreeNode(2))

assert(s.diameterOfBinaryTree(root) == 1)
