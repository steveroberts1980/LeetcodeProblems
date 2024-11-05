# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # We can just iterate through checking the value.
        # If the current value is greater than current node, 
        # check the next node. If the value is smaller than next,
        # insert here. If not, current = next.

        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        
        # if head does not contain a next
        # then add the new node right after and point to the head.
        if not head.next or head.next == head:
            head.next = Node(insertVal)
            head.next.next = head
            return head

        cur_node = head
        while True:
            if (insertVal >= cur_node.val and insertVal <= cur_node.next.val) or \
                (cur_node.val > cur_node.next.val and insertVal <= cur_node.next.val) or \
                cur_node.next == head:
                tmp = cur_node.next
                cur_node.next = Node(insertVal)
                cur_node.next.next = tmp
                break

            cur_node = cur_node.next

        return head        


s = Solution()

s.insert(Node(1), 0)