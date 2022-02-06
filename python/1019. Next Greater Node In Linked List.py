# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        # output = []
        # curr1 = head
        # while curr1 != None:
        #     curr2 = curr1.next
        #     while curr2 != None:
        #         if curr2.val > curr1.val:
        #             output.append(curr2.val)
        #             break
        #         curr2 = curr2.next
        #     if curr2 == None:
        #         output.append(0)
        #     curr1 = curr1.next
        # return output
        
        n = 0
        curr = head
        while curr != None:
            n += 1
            curr = curr.next
        
        out = [0] * n
        stack = []
        index = 0
        stack.append((head.val,index))
        curr = head.next
        while curr != None:
            while len(stack) != 0 and curr.val > stack[-1][0]:
                ele,ind = stack.pop()
                out[ind] = curr.val
            index += 1
            stack.append((curr.val,index))
            curr = curr.next
        
        return out
