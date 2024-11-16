# https://leetcode.com/problems/construct-binary-tree-from-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        root = TreeNode()
        stack = [root]
        i = 0
        
        while i < len(s):
            node = stack.pop()

            if s[i].isdigit() or s[i] == '-':
                num, i = self.get_num(s, i)

                node.val = num

                if i < len(s) and s[i] == '(':
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)
            elif node.left and s[i] == '(':
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)

            i += 1

        return stack.pop() if stack else root
    
    def get_num(self, s: str, i: int) -> tuple[int, int]:
        positive = True

        # check if the number is negative
        if s[i] == '-':
            positive = False
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        return (num if positive else -1 * num, i)


    def get_tree(self, root: TreeNode) -> List[int]:
        # Use bfs to print the tree
        result = []
        queue = deque()
        queue.append(root)

        while queue:

            node = queue.popleft()

            result.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return result

s = Solution()

root = s.str2tree("4(2(3)(1))(6(5))")
print(s.get_tree(root))

root = s.str2tree("4(2(3)(1))(6(5)(7))")
print(s.get_tree(root))

root = s.str2tree("-4(2(3)(1))(6(5)(7))")
print(s.get_tree(root))

