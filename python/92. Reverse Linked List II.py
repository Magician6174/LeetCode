# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        n = 1
        curr = head
        prev = None
        while curr != None:
            if n == left:
                break
            prev = curr
            curr = curr.next
            n += 1
        start_head = curr
        prev_start_head = prev
        prev = curr
        curr = curr.next
        for i in range(right - left):
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start_head.next = curr
        if prev_start_head == None:
            return prev
        else:
            prev_start_head.next = prev
        
        return head
