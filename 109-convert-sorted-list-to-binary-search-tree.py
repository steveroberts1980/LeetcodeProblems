# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&status=TO_DO%2CATTEMPTED&difficulty=EASY%2CMEDIUM

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []

        cur_node = head

        # First, get the linked list into a list so we can recursively build the tree
        while cur_node:
            vals.append(cur_node.val)
            cur_node = cur_node.next

        def buildTree(vals, start, end) -> TreeNode:
            if start > end:
                return None

            mid = math.ceil((start + end) / 2)

            node = TreeNode(vals[mid])
            node.left = buildTree(vals, start, mid-1)
            node.right = buildTree(vals, mid+1, end)

            return node

        return buildTree(vals, 0, len(vals) - 1)


s = Solution()

head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))

root = s.sortedListToBST(head)

print(root)
