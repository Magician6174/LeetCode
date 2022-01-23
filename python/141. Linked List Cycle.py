# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         self.current = head
#         li = []
#         while self.current != None:
#             if self.current.next not in li:
#                 li.append(self.current.next)
#             else:
#                 return True
#             self.current = self.current.next
#         return False
        
        fastptr = head
        slowptr = head
        while fastptr != None and slowptr !=None and fastptr.next != None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                return True
            
        return False
