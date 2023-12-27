# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        retVal = None
        head = None
        carry = 0

        while l1 and l2:
            if not retVal:
                retVal = ListNode((l1.val + l2.val) % 10)
                head = retVal
            else:
                retVal.next = ListNode((l1.val + l2.val + carry) % 10)
                retVal = retVal.next
            
            carry = math.floor((l1.val + l2.val + carry) / 10)
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                retVal.next = ListNode((l1.val + carry) % 10)
                carry = math.floor((l1.val + carry) / 10)
                retVal = retVal.next
                l1 = l1.next
        else:
            while l2:
                retVal.next = ListNode((l2.val + carry) % 10)
                carry = math.floor((l2.val + carry) / 10)
                retVal = retVal.next
                l2 = l2.next

        if carry > 0:
            retVal.next = ListNode(carry)

        return head