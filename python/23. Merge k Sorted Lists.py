# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
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
        
        ans = None
        for i in range(len(lists)):
            ans = merge2Lists(lists[i],ans)
        
        return ans
        
