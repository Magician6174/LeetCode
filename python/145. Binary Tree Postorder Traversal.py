# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return
        stack = []
        prev = None
        stack.append(root)
        output = []
        while stack:
            current = stack[-1]
            if prev is None or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    stack.pop()
                    output.append(current.val)
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
            else:
                output.append(current.val)
                stack.pop()
            prev = current
        
        return output

        
        
        
        """--------------------TC - O(n) SC - O(n)"""
#         if root is None:
#             return
#         recursive_stack = []
#         result_stack = []
#         recursive_stack.append(root)
#         while recursive_stack:
#             current = recursive_stack.pop()
#             if current.left:
#                 recursive_stack.append(current.left)
#             if current.right:
#                 recursive_stack.append(current.right)
#             result_stack.append(current)
        
#         output = []
#         while result_stack:
#             current = result_stack.pop()
#             output.append(current.val)
#         return output
