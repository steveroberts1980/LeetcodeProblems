# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List, Optional, Deque
import math
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create an array of arrays
        # keep a pointer to where we are in relation to the root node
        # i.e. -1 = left, +1 = right. As we traverse left, decrement and as we traverse right, increment. 
        # Use the pointer to know which index of the array to put the node value in.
        # the furthest down we can go is 7 levels. This would give 9 total spots.
        # we will start at index 4. This will be the root node or center.
        nodeList = defaultdict(list)
        q = deque()
        min_index, max_index = 0, 0

        if not root:
            return []

        q.append((root, 0))

        while(q):
            node, index = q.popleft()

            if not node:
                continue

            min_index = min(min_index, index)
            max_index = max(max_index, index)

            nodeList[index].append(node.val)

            q.append((node.left, index - 1))
            q.append((node.right, index + 1))

        retVal = []

        for n in range(min_index, max_index + 1):
            retVal.append(nodeList[n])

        return retVal


        

s = Solution()

ex1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ex2 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))

print(s.verticalOrder(ex1))