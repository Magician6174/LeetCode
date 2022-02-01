# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def kreverse(head_, k):
            n = 0
            temp = head_
            while temp != None:
                n+=1
                temp = temp.next
            if n >= k:
                curr = head_
                prev = None
                count = 0
                while curr != None and count < k:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                    count += 1
                if head_ != None:
                    head_.next = curr
                if curr != None:
                    curr = kreverse(curr,k)
                    head_.next = curr
                return prev
            else:
                return head_
        
        return kreverse(head,k)
            
            
