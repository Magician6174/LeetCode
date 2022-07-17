# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def search_(self,inorder,si,ei,key):
        
        # i_l = inorder[si:ei+1]
        for i,k in enumerate(inorder):
            if k == key:
                return i
            
    
    
    def helper(self,inorder,postorder,si,ei,sp,ep):
        
        if si > ei:
            return None
        if si == ei:
            return TreeNode(inorder[si])
        
        n = TreeNode(postorder[ep])
        idx = self.search_(inorder,si,ei,postorder[ep])
        # print(idx)
        n.left = self.helper(inorder,postorder, si, idx-1, sp, sp+idx-1-si)
        n.right = self.helper(inorder,postorder,idx+1,ei,sp+idx-si,ep-1)
        return n
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        return self.helper(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
