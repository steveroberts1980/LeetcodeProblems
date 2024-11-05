# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO%2CATTEMPTED&role=full-stack

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        retVal = []
        # BFS
        q = deque()
        q.append((root, 0))

        while q:
            n, depth = q.popleft()

            if not n:
                continue

            q.append((n.left, depth+1))
            q.append((n.right, depth+1))

            if len(retVal) < depth + 1:
                retVal.append(n.val)
            else:
                retVal[depth] = n.val

        return retVal

s = Solution()

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))

assert(s.rightSideView(root) == [1,3,4])

root = TreeNode(1, None, TreeNode(3))

assert(s.rightSideView(root) == [1,3])

root = []

assert(s.rightSideView(root) == [])

