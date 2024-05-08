from typing import Optional, List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeLists(self, l1, l2):
        dummy = ListNode()

        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return []
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))

            lists = mergedList
        return lists[0]


s = Solution()

list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

result = s.mergeKLists([list1, list2, list3])

r = result
checkVal = []
while r:
    checkVal.append(r.val)
    r = r.next

assert(checkVal == [1,1,2,3,4,4,5,6])
assert(s.mergeKLists([]) == [])
assert(s.mergeKLists([[]]) == [])