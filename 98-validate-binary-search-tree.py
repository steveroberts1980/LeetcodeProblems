# https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def checkNodes(node, left_bound, right_bound):
            if not node:
                return True
            
            if not (node.val > left_bound and node.val < right_bound):
                return False

            return checkNodes(node.left, left_bound, node.val) and checkNodes(node.right, node.val, right_bound)
        
        return checkNodes(root, float("-inf"), float("inf"))


s = Solution()

root = TreeNode(2, TreeNode(1), TreeNode(3))

assert(s.isValidBST(root))

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

assert(not s.isValidBST(root))

assert(s.isValidBST(None))