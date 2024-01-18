# https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if not p and not q:
                return True
            elif (not p and q) or (p and not q):
                return False
            
            return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # BFS to find the matching root.
        q = collections.deque()

        q.append(root)

        while q:
            node = q.pop()

            
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False



s = Solution()

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

assert(s.isSubtree(root, subRoot))

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

assert(not s.isSubtree(root, subRoot))

