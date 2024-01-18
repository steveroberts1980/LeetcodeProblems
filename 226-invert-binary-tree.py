# https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def printTree(root: TreeNode):
    s = []
    retVal = []

    if not root:
        return retVal

    s.insert(0, root)

    while len(s) > 0:
        node = s.pop()

        retVal.append(node.val)

        if node.left:
            s.insert(0, node.left)
        
        if node.right:
            s.insert(0, node.right)    

    return retVal

s = Solution()

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

result = s.invertTree(root)

assert(printTree(result) == [4,7,2,9,6,3,1])

root = TreeNode(2, TreeNode(1), TreeNode(3))

result = s.invertTree(root)

assert(printTree(result) == [2,3,1])

root = None

result = s.invertTree(root)

assert(printTree(result) == [])