# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        print(head)
        print(head.next.next)
        ptr = head
        print(ptr)
        result = head.next
        
        while ptr.next != None: # ptr 다음 null 일때까지
#             if ptr.next.next == None:
            
            if ptr.next.next == None or ptr.next.next.next == None:
                temp = ptr.next
                ptr.next = temp.next
                temp.next = ptr
                print('if')
                print(temp)
                break
            
            else:
                temp = ptr.next         #2
                first = temp.next       #3
                temp.next = ptr         
                ptr.next = first.next
                
                ptr=first
                print('else')
                print(temp)
                print(ptr)
            # else:
            #     temp = ptr.next
            #     ptr.next = temp.next
            #     temp.next = ptr
            #     print(temp)
            #     break

            
        return result