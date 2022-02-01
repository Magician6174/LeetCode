# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge2Lists(head1,head2):
            
            if head1 == None:
                return head2
            if head2 == None:
                return head1
            
            if head1.val <= head2.val:
                mergedList = head1
                head1 = head1.next
            else:
                mergedList = head2
                head2 = head2.next
                
            temp = mergedList
            
            while head1 != None and head2 != None:
                
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next
                    temp = temp.next
                else:
                    temp.next = head2
                    head2 = head2.next
                    temp = temp.next
            
            if head1 != None:
                temp.next = head1
            else:
                temp.next = head2
            
            return mergedList
        
        def dividelist(head):
            
            slow_ptr = head
            fast_ptr = head
            while fast_ptr.next != None and fast_ptr.next.next != None:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            start_second = slow_ptr.next
            slow_ptr.next = None
            return start_second
        
        def mergesort(head):
            if head != None and head.next != None:
                
                start_first = head
                start_second = dividelist(head)
                start_first = mergesort(start_first)
                start_second = mergesort(start_second)
                start_merged = merge2Lists(start_first, start_second)
                
                return start_merged
            else:
                return head
        
        return mergesort(head)
            
                
                
                
                
                
                
        
