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
    
    def helper(self,inorder,preorder,si,ei,sp,ep):
        
        if si > ei:
            return None
        if si == ei:
            return TreeNode(inorder[si])
        
        n = TreeNode(preorder[sp])
        idx = self.search_(inorder,si,ei,preorder[sp])
        # print(idx)
        n.left = self.helper(inorder,preorder, si, idx-1, sp+1, sp+idx-si)
        n.right = self.helper(inorder,preorder,idx+1,ei,sp+1+idx-si,ep)
        return n
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        return self.helper(inorder,preorder,0,len(inorder)-1,0,len(preorder)-1)
