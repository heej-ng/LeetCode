# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ptr = ListNode(0)
        n = k
        stack = []
        while head:
            if n == 0:
                for i in range(len(stack)):
                    ptr.next = ListNode(stack.pop())
                    ptr = ptr.next
                n = k
            if n > 0:
                stack.append(head.val)
                n -= 1
            head = head.next
        if k == len(stack):
            for i in range(len(stack)):
                ptr.next = ListNode(stack.pop())
                ptr = ptr.next
        else:
            for remain in stack:
                ptr.next = ListNode(remain)
                ptr = ptr.next
        return result.next