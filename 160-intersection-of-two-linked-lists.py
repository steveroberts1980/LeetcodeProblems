# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=hash-table

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = headA
        n2 = headB

        while n1 != n2:
            if not n1:
                n1 = headB
            else:
                n1 = n1.next
            if not n2:
                n2 = headA
            else:
                n2 = n2.next

        return n1

s = Solution()

