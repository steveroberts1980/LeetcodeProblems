# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_copies = {}

        def copy_node(n):
            nonlocal node_copies

            if not n:
                return None
            
            if n in node_copies:
                return node_copies[n]

            tmp = Node(n.val)
            node_copies[n] = tmp
            tmp.next = copy_node(n.next)
            tmp.random = copy_node(n.random)

            return tmp
        
        return copy_node(head)


# Use a hashset to keep track of the node copies for each node
# Recursively copy until the end is reached.
# When the last node does not have a next, we are finished.