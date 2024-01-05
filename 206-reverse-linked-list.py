# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        next = head.next
        head.next = None
        while (next):
            tmp = next
            next = tmp.next
            tmp.next = head
            head = tmp
        return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = s.reverseList(head)

assert(s.reverseList([1,2,3,4,5]) == [5,4,3,2,1])
assert(s.reverseList([1,2]) == [2,1])
assert(s.reverseList([]) == [])
