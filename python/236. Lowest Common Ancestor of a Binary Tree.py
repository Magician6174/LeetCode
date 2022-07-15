# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return
        if root.val == p.val or root.val == q.val:
            return root
        
        leftSearch = self.lowestCommonAncestor(root.left,p,q)
        rightSearch = self.lowestCommonAncestor(root.right,p,q)
        
        if leftSearch is None:
            return rightSearch
        if rightSearch is None:
            return leftSearch
        if leftSearch.val == p.val and rightSearch.val == q.val:
            return root
        if leftSearch.val == q.val and rightSearch.val == p.val:
            return root 
        return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = [root]
#         dfs = []
#         pred = {}
#         while stack:
#             if root:
#                 dfs.append(root.val)
#                 stack.append(root)
#                 if root.left:
#                     pred[root.left.val] = root.val
#                 root = root.left
                
#             else:
#                 t = stack.pop()
#                 if t.right:
#                     pred[t.right.val] = t.val
#                     root = t.right
#         # print(dfs)
#         print(pred)
#         p_pred = [p.val]
#         pr = 4
#         while pr in pred.keys():
#             pr = pred[pr]
#             p_pred.append(pr)
#         q_pred = [q.val]
#         qr = 6
#         while qr in pred.keys():
#             qr = pred[qr]
#             q_pred.append(qr)
#         print(p_pred)
#         print(q_pred)
