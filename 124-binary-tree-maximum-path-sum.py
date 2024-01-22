# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        global res 
        res = root.val

        def search(node):
            if not node:
                return 0
            
            global res
            
            left_max = max(search(node.left), 0)
            right_max = max(search(node.right), 0)

            # What is the value if allowed to split?
            res = max(res, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)
            
        search(root)

        return res


s = Solution()

root = TreeNode(1, TreeNode(2), TreeNode(3))

assert(s.maxPathSum(root) == 6)

root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

assert(s.maxPathSum(root) == 42)

