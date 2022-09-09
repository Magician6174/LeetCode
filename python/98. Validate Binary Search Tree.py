# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """---------------Iterative approach------------------"""
        if not root:
            return True
        
        stack = [(root,float('-inf'),float('+inf'))]
        
        while stack:
            root,lower,upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right,val,upper))
            stack.append((root.left,lower,val))
            
        return True
        
        """-------------Recursive approach-----------------"""
#         def check(root,lower,upper):
#             if root is None:
#                 return True
#             val = root.val
#             if val <= lower or val >= upper:
#                 return False
#             if not check(root.left,lower,val):
#                 return False
#             if not check(root.right,val,upper):
#                 return False
#             return True
            
#         lower = float('-inf')
#         upper = float('+inf')
        
#         return check(root,lower,upper)
        
        
        """-----------Approach 1------------------"""
#         output = []
#         output = self.inorder(root,output)
        
#         for i in range(1,len(output)):
#             if output[i-1] >= output[i]:
#                 return False
#         return True
    
#     def inorder(self,root,output):
        
#         if root is None:
#             return 
#         self.inorder(root.left,output)
#         output.append(root.val)
#         self.inorder(root.right,output)
#         return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         if root.left is None and root.right is None:
#             return True
#         if root.left and root.right:
#             if root.val > root.left.val and root.val < root.right.val:
#                 return self.isValidBST(root.left) and self.isValidBST(root.right)
#             else:
#                 return False
#         elif root.left:
#             if root.val > root.left.val:
#                 return self.isValidBST(root.left)
#             return False
#         elif root.right:
#             if root.val < root.right.val:
#                 return self.isValidBST(root.right)
#             return False
        
        
