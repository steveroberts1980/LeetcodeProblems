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
        # if we get back to the head, insert there

        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        
        prev = head
        cur_node = head.next
        
        while True:
            if prev == cur_node or (cur_node == head) or (prev.val <= insertVal and cur_node.val >= insertVal) or (prev.val > cur_node.val and (insertVal <= cur_node.val or insertVal >= prev.val)):
                prev.next = Node(insertVal)
                prev.next.next = cur_node
                break

            prev = cur_node
            cur_node = prev.next

        return head        


s = Solution()

head = Node(3, Node(5, Node(1)))
head.next.next.next = head

head = s.insert(head, 6)

head = Node(3, Node(4, Node(1)))
head.next.next.next = head

head = s.insert(head, 2)

head = None
head = s.insert(head, 1)

head = Node(1)
head.next = head

head = s.insert(head, 0)
exit(0)