# https://leetcode.com/problems/linked-list-cycle-ii/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        seenNodes = set()

        node = head

        while node.next:
            if node in seenNodes:
                return node
            
            seenNodes.add(node)
            node = node.next
    
        return None


s = Solution()

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

assert(s.detectCycle(head).val == 2)
