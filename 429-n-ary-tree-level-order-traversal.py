# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        q = deque()

        if not root:
            return output
        
        q.append((root, 0))
        level_vals = []
        while q:
            node, level = q.popleft()

            if level > len(output):
                output.append(level_vals.copy())
                level_vals = []
            
            level_vals.append(node.val)

            if node.children:
                for child in node.children:
                    q.append((child, level+1))

        output.append(level_vals)

        return output


s = Solution()


root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

assert(s.levelOrder(root) == [[1],[3,2,4],[5,6]])

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])

assert(s.levelOrder(root) == [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])