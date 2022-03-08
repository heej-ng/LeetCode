# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        total_cnt = 0
        while ptr:
            total_cnt += 1
            ptr = ptr.next
        print(total_cnt)
        cnt = total_cnt - n
        
        if cnt == 0:
            return head.next
        
        ptr = head
        while ptr:
            if cnt == 1:
                print(ptr)
                temp = ptr.next.next
                ptr.next = temp
                break
            ptr = ptr.next
            cnt -= 1
        return head
        