# https://leetcode.com/problems/same-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

s = Solution()

t1 = TreeNode(1, TreeNode(2), TreeNode(1))
t2 = TreeNode(1, TreeNode(1), TreeNode(2))

assert(not s.isSameTree(t1, t2))

t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))
assert(s.isSameTree(t1, t2))

t1 = TreeNode(1, TreeNode(2))
t2 = TreeNode(1, None, TreeNode(2))

assert(not s.isSameTree(t1, t2))

