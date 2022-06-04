# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q:
            if p.val != q.val:
                return False
            ltree = self.isSameTree(p.left,q.left)
            rtree = self.isSameTree(p.right,q.right)
            if ltree and rtree:
                return True
            else: 
                False
        if p and not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True

        
