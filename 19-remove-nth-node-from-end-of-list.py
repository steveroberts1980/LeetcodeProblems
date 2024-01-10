# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate to end and push each node to a stack.
        # Pop n+1 items keeping track of n+1, n and n-1
        # set n+1.next to n-1.next

        # Edge cases: 1 item in list, no items in list
        node = head
        stack = []

        if not head.next:
            return None

        # Fill the stack
        while node:
            stack.append(node)
            node = node.next

        before_remove = None
        to_remove = None
        after_remove = None

        # If we are removing the first node, just return the list after that.
        if n == len(stack):
            return head.next

        for i in range(n+1):
            after_remove = to_remove
            to_remove = before_remove
            before_remove = stack.pop()

        before_remove.next = after_remove

        return head

                
# After watching the neetcode video
# Try one with 2 pointers. A fast pointer and a slow pointer with n between them.
    

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = s.removeNthFromEnd(head, 2)

output = []
while (result):
    output.append(result.val)
    result = result.next

assert(output == [1,2,3,5])

head = ListNode(1)

result = s.removeNthFromEnd(head, 1)

output = []
while (result):
    output.append(result.val)
    result = result.next

assert(output == [])

head = ListNode(1)
head.next = ListNode(2)

result = s.removeNthFromEnd(head, 1)

output = []
while (result):
    output.append(result.val)
    result = result.next

assert(output == [1])
