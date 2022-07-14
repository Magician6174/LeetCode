# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        
        queue = []
        output = []
        queue.append(root)
        output.append([root.val])
        while queue:
            
            o = []
            for i in range(len(queue)):
                top = queue.pop(0)
                if top.left:
                    queue.append(top.left)
                    o.append(top.left.val)
                if top.right:
                    queue.append(top.right)
                    o.append(top.right.val)
            output.append(o)
        return output[::-1][1:]
                
