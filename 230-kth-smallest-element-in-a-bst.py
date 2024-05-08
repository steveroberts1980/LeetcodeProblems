from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #Using the stack approach as was discussed
        stack = []
        count = 0
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            count += 1
            if count == k:
                return node.val

            node = node.right

s = Solution()

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))

assert(s.kthSmallest(root, 1) == 1)

root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))

assert(s.kthSmallest(root, 3) == 3)
