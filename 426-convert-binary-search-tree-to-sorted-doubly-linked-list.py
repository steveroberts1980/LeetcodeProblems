# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        stack = []
        current = root
        first = None
        last = None

        # In order traversal
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()

                if not first:
                    first = current

                if last:
                    last.right = current
                    current.left = last

                last = current    
                current = current.right

        last.right = first
        first.left = last

        return first

s = Solution()

root = Node(4, Node(2, Node(1), Node(3)), Node(5))

node = s.treeToDoublyList(root)

for i in range(5):
    print(node.val)
    node = node.right

