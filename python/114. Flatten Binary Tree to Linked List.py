# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.helper(root)
    def helper(self,root):
        if root is None:
            return
        self.helper(root.right)
        self.helper(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        
        
        
