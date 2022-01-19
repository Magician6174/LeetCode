# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1 =[]
        li2 =[]
        while True:
            li1.append(l1.val)
            if l1.next != None:
                
                l1 = l1.next
            else:
                break
        while True:
            li2.append(l2.val)
            if l2.next != None:
                
                l2 = l2.next
            else:
                break
        
        
        li1.reverse()
        li2.reverse()

        a = ''.join(map(str, li1))
        b = ''.join(map(str, li2))
        c = int(a) + int(b)
        c = str(c)
        
        
        c = [int(x) for x in c]
        
        
        # o = ListNode(val = c[0],next = ListNode(val = c[1],next = ListNode(val=c[2])))
        o = ListNode(val = c[0])
        for i in range(len(c)-1):
            o = ListNode(val = c[i+1],next = o)
    
        print(o)
        return o
     
        
        
        