# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        while curr != None and curr.next != None:
            temp = curr.next
            while temp != None and curr.val == temp.val:
                temp = temp.next
            curr.next = temp
            curr = curr.next
        return head
