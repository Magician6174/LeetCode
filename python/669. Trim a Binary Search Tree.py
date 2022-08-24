# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if root is None:
            return
        
        if root.val >= low and root.val <= high:
            if root.left and root.left.val < low:
                root.left = root.left.right
            if root.right and root.right.val > high:
                root.right = root.right.left
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            return root
        elif root.val < low:
            return self.trimBST(root.right,low,high)
        else:
            return self.trimBST(root.left,low,high)
        
