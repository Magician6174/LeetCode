# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h = 0
        self.diam = 0
        print(self.heightBT(root))
        return self.diam
        
        
        
    def heightBT(self,root):
        
        if root is None:
            return -1
        lHeight = self.heightBT(root.left)
        rHeight = self.heightBT(root.right)
        self.diam = max(self.diam,lHeight+rHeight+2)
        return max(lHeight,rHeight)+1
        
