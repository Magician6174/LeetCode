# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """---------------Iterative Approach-----------------"""
        
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k==0:
                return root.val
            root = root.right
        
        
        
        
        
        
        
        
        """---------------------Using Inorder Traversal--------------------"""
#         self.ans = []
#         self.inorder(root)
#         return self.ans[k-1]
    
#     def inorder(self,root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         self.ans.append(root.val)
#         self.inorder(root.right)
