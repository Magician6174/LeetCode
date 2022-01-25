# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fp = head
        sp = head
        flag = False
        while fp != None and fp.next != None:
            
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                flag = True
                break
        """Great explanation!
            But the math part missed the case when fast cycled through the loop multiple times before meeting slow.
            The math part should be:
            What is the distance fast moved? What is the distance slow moved? And their relationship?

            x1+x2
            x1+n(x2+x3)+x2
            x1+n(x2+x3)+x2=2(x1+x2)

            Here n is an integer greater than or equal to 0.
            And x2+x3 is the length of the loop.
            Then we can get:

            x1=(n-1)x2+nx3

            After resetting slow, they will meet at the start of the loop.
            This is because when slow moved x1, fast moved (x1+n(x2+x3)+x2)+((n-1)x2+nx3) = x1 + 2n(x2+x3)"""
        if flag:
            node = head
            while node != sp:
                node = node.next
                sp = sp.next
            return node
        
        return None
