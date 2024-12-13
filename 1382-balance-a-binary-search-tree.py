# https://leetcode.com/problems/balance-a-binary-search-tree/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodeVals = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            nodeVals.append(node.val)
            traverse(node.right)

        def createBalancedBST(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2

            node = TreeNode(nodeVals[mid])
            
            #now run this on the left and right
            node.left = createBalancedBST(start, mid-1)
            node.right = createBalancedBST(mid+1, end)

            return node

        traverse(root)
        returnNode = createBalancedBST(0, len(nodeVals) - 1)

        return returnNode
        
s = Solution()

root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
n = s.balanceBST(root)


root = TreeNode(2, TreeNode(1), TreeNode(3))
n = s.balanceBST(root)
