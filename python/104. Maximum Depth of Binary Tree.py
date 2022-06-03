# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """------------Recursive Approach--------------"""
        # if root is None:
        #     return 0
        # else:
        #     ldepth = self.maxDepth(root.left)
        #     rdepth = self.maxDepth(root.right)
        #     return 1 + max(ldepth,rdepth)
        """ ----------------Iterative Approach-----------------"""
        stack = []
        if root:
            stack.append((1,root))
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth,current_depth)
                stack.append((current_depth+1,root.left))
                stack.append((current_depth+1,root.right))
        return depth
