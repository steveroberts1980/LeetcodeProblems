# https://leetcode.com/problems/linked-list-cycle/

######################################
# Linked List
######################################

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        ptr1, ptr2 = head, head

        while ptr1.next and ptr2.next and ptr2.next.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

            if ptr1 == ptr2 and ptr1.next and ptr2.next:
                return True

        return False

# Neetcode suggested using a hashtable to track. This implementation is to test that out.
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        track_hash = {}

        node = head

        while node:
            if track_hash.get(node, False):
                return True
            
            track_hash[node] = True

            node = node.next
        
        return False

s = Solution2()

head = ListNode(3)
cycled = ListNode(2)
head.next = cycled
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = cycled
print(s.hasCycle(head))

head.next.next.next.next = None
print(s.hasCycle(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(s.hasCycle(head))

head = ListNode(1)
print(s.hasCycle(head))

print(s.hasCycle(None))