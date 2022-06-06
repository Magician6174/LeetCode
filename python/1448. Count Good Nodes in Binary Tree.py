# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self,root, m):
        if root is None:
            return 0
        maximum = max(root.val,m)
        c = (root.val >= maximum)
        return c + self.check(root.left, maximum) + self.check(root.right,maximum)
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.check(root,root.val)
            
            
