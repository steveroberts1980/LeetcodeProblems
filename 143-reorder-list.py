# https://leetcode.com/problems/reorder-list/

######################################
# Linked List
######################################

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Algo: 
            # Find middle of list with a fast and slow pointer.
            # Reverse the 2nd list
            # Combine the 2 lists
        
        if not head.next:
            return
        
        slow = head
        fast = head.next
        
        # Find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now reverse the 2nd list
        # Split the list into 2
        new_head = slow.next
        slow.next = None
        new_tail = None

        while new_head:
            tmp = new_head.next
            new_head.next = new_tail
            new_tail = new_head
            new_head = tmp

        # Now recombine the 2 lists
        l1 = head
        l2 = new_tail
        while l2:
            tmp = l1.next
            l1.next = l2
            
            l2 = l2.next
            l1 = l1.next
            l1.next = tmp
            l1 = l1.next

s = Solution()

# l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# s.reorderList(l)

# n = l
# while n:
#     print(n.val)
#     n = n.next

# print('-----------')
# l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# s.reorderList(l)

# n = l
# while n:
#     print(n.val)
#     n = n.next

print('-----------')
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

s.reorderList(l)

n = l
while n:
    print(n.val)
    n = n.next
