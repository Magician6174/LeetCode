# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if head == None or head.next == None or head.next.next == None:
            return head
        o = head
        e = head.next
        eh = head.next
        
        while o.next and e.next:
            if o.next.next:
                o.next = o.next.next
                o = e.next
            if e.next.next:
                e.next = e.next.next
                e = o.next
            else:
                e.next = None
                break
            
        o.next = eh
        return head
