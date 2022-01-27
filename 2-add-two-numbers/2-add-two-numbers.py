# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = out = ListNode(0)
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp -= 10
            ptr.next = ListNode(temp)
            l1 = l1.next
            l2 = l2.next
            ptr = ptr.next
        while carry == 1:
            temp = 0
            if l1 != None:
                temp = l1.val + carry
                l1 = l1.next
            elif l2 != None:
                temp = l2.val + carry
                l2 = l2.next
            else:
                temp = carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp -= 10
            ptr.next = ListNode(temp)
            ptr = ptr.next
        if l1 != None:
            ptr.next = l1
        elif l2 != None:
            ptr.next = l2
        return out.next