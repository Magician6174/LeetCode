# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sum_left_nodes(root,isleft):
            
            if root is None:
                return 0
            if root.left is None and root.right is None and isleft:
                print(root.val)
                return root.val
            return sum_left_nodes(root.left,True) + sum_left_nodes(root.right,False)
        return sum_left_nodes(root,False)
