# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def lastkthnode(head,k):
            if head.next == None:
                return None
            temp1=head
            temp2=head
            count = 0
            for i in range(k):
                try:
                    temp1=temp1.next
                except:
                    return -1
                
            while temp1 is not None:
                temp1=temp1.next
                temp2=temp2.next
            return temp2
        
        lastK_plus_1 = lastkthnode(head,n+1)
        print(lastK_plus_1)
        if lastK_plus_1 == -1:
            head = head.next
        elif lastK_plus_1 != None:
            lastK_plus_1.next = lastK_plus_1.next.next
        else:
            head = None
        return head
