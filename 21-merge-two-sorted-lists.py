# https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = ListNode()

        while (list1 or list2):
            if not list1:
                node.next = ListNode(list2.val)
                list2 = list2.next
            elif not list2:
                node.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next

            if not head:
                head = node.next

            node = node.next
                
        return head



s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

head = s.mergeTwoLists(l1, l2)

output = []
while (head):
    output.append(head.val)
    head = head.next

assert(output == [1,1,2,3,4,4])

head = s.mergeTwoLists(None, None)
output = []
while (head):
    output.append(head.val)
    head = head.next

assert(output == [])

l1 = None
l2 = ListNode(0)
head = s.mergeTwoLists(l1, l2)

output = []
while (head):
    output.append(head.val)
    head = head.next

assert(output == [0])
