# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.output = []
        path = []
        self.dfs(root,path)
        # print(self.output)
        ans = []
        for i in self.output:
            s = '->'.join(i)
            ans.append(s)
        return ans
        
    def dfs(self,root,path):
        path = list(path)
        if root:
            path.append(str(root.val))
        if root is None:
            return
        if root.left is None and root.right is None:
            self.output.append(path)
        self.dfs(root.left,path)
        self.dfs(root.right,path)
        
