# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class dfs:
    def __init__(self, root):
        self.stack = []
        self.cur_node = root
        self.results = []

        self.search()

    def search(self):
        while self.stack or self.cur_node:
            # process left
            if self.cur_node:
                self.stack.append(self.cur_node)
                self.cur_node = self.cur_node.left
            else:
                self.cur_node = self.stack.pop()
                self.results.append(self.cur_node.val)
                self.cur_node = self.cur_node.right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result = []

        # DFS to get the next node. Implement iterative approach and use get_next to return the next item.
        # We could also implement a peek on the class too.
        dfs1 = dfs(root1)
        dfs2 = dfs(root2)
        i = 0
        j = 0

        while i < len(dfs1.results) and j < len(dfs2.results):
            if dfs1.results[i] < dfs2.results[j]:
                result.append(dfs1.results[i])
                i += 1
            else:
                result.append(dfs2.results[j])
                j += 1
        
        while i < len(dfs1.results):
            result.append(dfs1.results[i])
            i += 1

        while j < len(dfs2.results):
            result.append(dfs2.results[j])
            j += 1

        return result

s = Solution()

root1 = TreeNode(2, TreeNode(1), TreeNode(4))
root2 = TreeNode(1, TreeNode(0), TreeNode(3))

print(s.getAllElements(root1, root2))

root1 = TreeNode(1, None, TreeNode(8))
root2 = TreeNode(8, TreeNode(1), None)

print(s.getAllElements(root1, root2))