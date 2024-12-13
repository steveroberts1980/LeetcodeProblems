# https://leetcode.com/problems/odd-even-linked-list/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()
        counter = 1
        cur_odd = odd_head
        cur_even = even_head

        cur_node = head
        while cur_node:
            if (counter % 2) == 1:
                cur_odd.next = cur_node
                cur_odd = cur_odd.next
            else:
                cur_even.next = cur_node
                cur_even = cur_even.next
            cur_node = cur_node.next
            counter += 1

        cur_even.next = None
        cur_odd.next = even_head.next

        return odd_head.next



s = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

head = s.oddEvenList(head)

cur_node = head
values = []
while cur_node:
    values.append(cur_node.val)
    cur_node = cur_node.next

print(values)