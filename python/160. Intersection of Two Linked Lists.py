# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
  
        # while headA != None:
        #     temp = headB
        #     while temp != None:
        #         if temp == headA:
        #             return headA
        #         else:
        #             temp = temp.next
        #     headA = headA.next
        # return None
        
        countA = 0
        countB = 0
        tempA = headA
        tempB = headB
        while tempA != None:
            countA += 1
            tempA = tempA.next
            
        while tempB != None:
            countB +=1
            tempB = tempB.next
        
        diff = countA - countB
        
        if diff>0:
            for i in range(diff):
                headA = headA.next
        else:
            for i in range(abs(diff)):
                headB = headB.next
        
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
                
        
