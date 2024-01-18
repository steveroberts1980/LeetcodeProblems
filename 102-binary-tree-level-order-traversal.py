# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        result = []

        q.append([root, 0])

        while len(q):
            node, level = q.pop()

            if len(result) < level + 1:
                result.append([])

            result[level].append(node.val)

            if node.left:
                q.insert(0, [node.left, level + 1])

            if node.right:
                q.insert(0, [node.right, level + 1])

        return result

# After watching neetcode, instead of keeping the level in an array, check the 
# queue length at the start and then use a for loop to process the length of the current queue.

s = Solution()


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

assert(s.levelOrder(root) == [[3],[9,20],[15,7]])

root = TreeNode(1)

assert(s.levelOrder(root) == [[1]])

root = None

assert(s.levelOrder(root) == [])