# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            if root is None:
                return
            if root.val not in d.keys():
                d[root.val] = 1
            else:
                d[root.val] += 1
            preorder(root.left)
            preorder(root.right)
        
        d = {}
        preorder(root)
        max_ = max(d.values())
        ans =[]
        for i in d.keys():
            if d[i] == max_:
                ans.append(i)
        return ans
        
