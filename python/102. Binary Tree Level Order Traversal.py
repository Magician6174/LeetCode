# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        queue = []
        levels = []
        level = 0
        queue.append(root)
        while queue:
            levels.append([])
            level_length = len(queue)
            
            for i in range(level_length):
                top = queue.pop(0)
                levels[level].append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            level += 1
        return levels
            
            
            
