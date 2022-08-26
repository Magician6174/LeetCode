# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.ans = []
        
        self.helper(root,0)
        return self.ans
    
    
    def helper(self,root,depth):
        
        if root:
            if len(self.ans) == depth:
                self.ans.append(root.val)

            self.helper(root.right,depth+1)
            self.helper(root.left,depth+1)
