"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.p = []
        self.preOrder(root)
        return self.p
        
    def preOrder(self,root):
        if root is None:
            return
        self.p.append(root.val)
        for i in root.children:
            self.preOrder(i)
