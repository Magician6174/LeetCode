"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        if curr == None:
            return
        while curr:
            # create intermediate node between every pair of node
            temp = curr.next
            temp1 = Node(curr.val)
            temp1.next = None
            temp1.prev = None
            curr.next = temp1
            curr.next.next = temp
            curr = temp

        # Adjust prev pointer for new copy-nodes created in the previous step
        curr = head
        while curr:
            if curr.next:
                if curr.random:
                    curr.next.random = curr.random.next
                else:
                    curr.next.random = curr.random
            if curr.next:
                curr = curr.next.next
            else:
                curr = curr.next

        # split the combined list into original list and copy list
        original = head
        copy = head.next

        temp = copy

        while original and copy:
            if original.next:
                original.next = original.next.next
            else:
                original.next = original.next

            if copy.next:
                copy.next = copy.next.next
            else:
                copy.next = copy.next

            original = original.next
            copy = copy.next

        return temp



