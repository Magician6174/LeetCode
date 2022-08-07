# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.output = []
        path = []
        self.dfs(root,path)
        print(self.output)
        sum = 0
        for i,rootToLeaf in enumerate(self.output):
            number = ''.join(rootToLeaf)
            sum += int(number)
        return sum
        
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
