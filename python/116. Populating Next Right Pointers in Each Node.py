"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return
        queue = [root]
        while queue:
            
            for i in range(len(queue)):
                if i < len(queue)-1:
                    queue[i].next = queue[i+1]

            for i in range(len(queue)):
                top = queue.pop(0)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            
        return root
    
                
        
                
            
