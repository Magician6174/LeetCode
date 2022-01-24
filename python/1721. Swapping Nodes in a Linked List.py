# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         if head != None and head.next != None:
#             beginning_node = head
#             ending_node = head
#             last_kth_node = head
#             if head.next.next == None:
#                     temp = head
#                     head = head.next
#                     head.next = temp
#                     head.next.next = None
#                     return head
#             if k == 1 or k:
#                 for i in range(k):
#                     ending_node = ending_node.next
#                 while ending_node != None:
#                     ending_node = ending_node.next
#                     prev_node = last_kth_node
#                     last_kth_node = last_kth_node.next
#                 temp = head
#                 head = last_kth_node
#                 head.next = temp.next
#                 prev_node.next = temp
#                 prev_node.next.next = None
#                 return head
#             beginning_node = head
#             ending_node = head
#             last_kth_node = head
#             for i in range(k-1):
#                 prev_beginning = beginning_node
#                 beginning_node = beginning_node.next
#             for i in range(k):
#                 ending_node = ending_node.next
#             while ending_node != None:
#                 ending_node = ending_node.next
#                 prev_node = last_kth_node
#                 last_kth_node = last_kth_node.next

#             prev_node.next = beginning_node
#             temp = beginning_node.next
#             beginning_node.next = last_kth_node.next
#             prev_beginning.next = last_kth_node
#             last_kth_node.next = temp


#         return head

        if head != None and head.next != None:
            b = head
            kth = head
            e = head
            for i in range(k-1):
                b = b.next
            for i in range(k):
                e = e.next
            while e != None:
                e = e.next
                kth = kth.next
            temp = b.val
            b.val = kth.val
            kth.val = temp
            # print(head)
            return head
        return head
                        
