# https://leetcode.com/problems/check-completeness-of-a-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        # Use BFS
        # When traversing, keep track of the current height and number of nodes. We should be 
        # able to determine that it is not complete if any of the node counts at 0 thru (h-1) are not 
        # equal to 2^h. On the last row, if we encounter any right nodes where the left is empty, then it 
        # is not complete
        q = deque()
        q.append((root, 0))
        node_count = 0
        expected_nodes = 0
        current_level = 0
        missing = False

        while q:
            node, level = q.popleft()

            # we are moving to a new level. See if the previous 
            # current node count is the expected count for the 
            # previous levels
            if current_level != level:
                expected_nodes += pow(2, current_level)
                if expected_nodes != node_count:
                    return False
                current_level = level

            # keep track of the nodes we've processed
            node_count += 1

            # if there is a right child but not left, then the tree is not complete
            if not node.left and node.right:
                return False
            
            if missing and (node.left or node.right):
                return False
            
            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

            if not node.left or not node.right:
                missing = True

        return True

s = Solution()

root = TreeNode(1, TreeNode(2, TreeNode(5), None), TreeNode(3, TreeNode(7), TreeNode(8)))

assert(not s.isCompleteTree(root))

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))

assert(s.isCompleteTree(root))

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))

assert(not s.isCompleteTree(root))

root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(7), TreeNode(8)))

assert(not s.isCompleteTree(root))