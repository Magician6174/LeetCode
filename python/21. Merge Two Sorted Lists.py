# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         head = None
        
#         while list1 != None and list2 != None:
            
#             if head == None:
#                 if list1.val < list2.val:
#                     head = list1
#                     list1 = list1.next
#                 else:
#                     head = list2
#                     list2 = list2.next
#                 curr = head
#             if list1 == None or list2 == None:
#                 break
#             if list1.val < list2.val:
#                 curr.next = list1
#                 list1 = list1.next
#             else:
#                 curr.next = list2
#                 list2 = list2.next
#             curr = curr.next
        
        
#         while list1 != None:
#             if head != None:
#                 curr.next = list1
#                 curr = curr.next
#             else:
#                 head = list1
#                 curr = head
#             list1 = list1.next

#         while list2 != None:
#             if head != None:
#                 curr.next = list2
#                 curr = curr.next
#             else:
#                 head = list2
#                 curr = head
#             list2 = list2.next

#         return head

        """------------------------INPLACE MERGING----------------------------"""
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            mergedList = list1
            list1 = list1.next
        else:
            mergedList = list2
            list2 = list2.next
        
        temp = mergedList
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                
        if list1 == None:
            temp.next = list2
        else:
            temp.next = list1
        return mergedList
        
