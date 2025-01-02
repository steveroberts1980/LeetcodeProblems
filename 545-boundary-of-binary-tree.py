# https://leetcode.com/problems/boundary-of-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        boundary = []

        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        boundary.append(root.val)

        # Now DFS for leafe nodes
        def dfs(node: TreeNode):
            if not node:
                return
            
            if not node.left and not node.right:
                boundary.append(node.val)
            
            dfs(node.left)
            dfs(node.right)

        # First, traverse the left side until we hit a leaf node
        curNode = root.left

        while curNode and (curNode.left or curNode.right):
            boundary.append(curNode.val)
            if curNode.left:
                curNode = curNode.left
            else:
                curNode = curNode.right

        # Get the leaf nodes
        dfs(root)
        
        # Finally, traverse the right side until we hit a leaf node
        curNode = root.right
        rightStack = []

        while curNode and (curNode.left or curNode.right):
            rightStack.append(curNode.val)
            if curNode.right:
                curNode = curNode.right
            else:
                curNode = curNode.left

        # Now that we have the results, pop all the items off to reverse the order.
        # Don't pop the last item since it is the root and we already captured that.
        while len(rightStack):
            boundary.append(rightStack.pop())

        return boundary

s = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
print(s.boundaryOfBinaryTree(root))
assert(s.boundaryOfBinaryTree(root) == [1,3,4,2])
       
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10))))

assert(s.boundaryOfBinaryTree(root) == [1,2,4,7,8,9,10,6,3])