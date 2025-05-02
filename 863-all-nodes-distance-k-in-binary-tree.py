# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&status=TO_DO&difficulty=EASY%2CMEDIUM&role=full-stack

from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        offsetsHash = {}
        graph = defaultdict(list)
        nodes = []

        # First, build the tree as a graph
        # Then DFS from the target node, keeping track of distance
        # Also, keep track to visited nodes in a set
        # Every node we visit that is at k distance, add to the return nodes
        # Also, once we are at a distance of k, we don't need to continue searching deeper

        def buildGraph(node, parent):
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                buildGraph(node.left, node)
            if node.right:
                buildGraph(node.right, node)

        buildGraph(root, None)
        visited = set()

        def dfs(node, depth):
            if depth == k:
                nodes.append(node)
                return

            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n, depth+1)

        visited.add(target.val)
        dfs(target.val, 0)

        print(nodes)
        return nodes



s = Solution()

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

assert(s.distanceK(root, TreeNode(5), 2) == [7,4,1])

root = TreeNode(1)
assert(s.distanceK(root, TreeNode(1), 3) == [])

