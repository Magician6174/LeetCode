# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode
        curr = head
        while curr != None:
            while curr.next and prev.next.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = curr
            else:
                prev.next = curr.next
            
            curr = curr.next
            
        
        return dummyNode.next
            
