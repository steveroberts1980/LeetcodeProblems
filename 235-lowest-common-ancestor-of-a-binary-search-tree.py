# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur



s = Solution()

root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

assert(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val == 6)

assert(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val == 2)

root = TreeNode(2)
root.left = TreeNode(1)

assert(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val == 2)
