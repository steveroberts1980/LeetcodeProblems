# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=hash-table

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indexes = {}
        preorder_index = 0

        for i in range(len(inorder)):
            inorder_indexes[inorder[i]] = i

        def parseTree(left, right) -> TreeNode:
            nonlocal preorder_index

            if left > right:
                return None
            
            rootVal = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(rootVal)

            inorderOffset = inorder_indexes[rootVal]
            root.left = parseTree(left, inorderOffset - 1)
            root.right = parseTree(inorderOffset + 1, right)

            return root

        return parseTree(0, len(preorder)-1)


s = Solution()


root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
root = s.buildTree([-1], [-1])