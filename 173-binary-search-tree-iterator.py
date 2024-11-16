# https://leetcode.com/problems/binary-search-tree-iterator/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = list()
        self.cur_node = self.root
        # DFS
        # Typically, DFS uses recursion
        # However, we can use a stack to implement
        # without recursion

    def print(self) -> None:
        stack = list()
        cur_node = self.root

        while (stack or cur_node):
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                print(cur_node.val)
                cur_node = cur_node.right


    def next(self) -> int:
        return_value = None
        while (self.stack or self.cur_node):
            if self.cur_node:
                self.stack.append(self.cur_node)
                self.cur_node = self.cur_node.left
            else:
                self.cur_node = self.stack.pop()
                return_value = self.cur_node.val
                self.cur_node = self.cur_node.right
                return return_value

    def hasNext(self) -> bool:
        return bool(self.stack or self.cur_node)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

s = BSTIterator(root)
print(s.next())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())


