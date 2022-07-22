# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node,par = None):
            if node:
                node.par = par
                dfs(node.left,node)
                dfs(node.right,node)
            
        dfs(root)
        
        queue = [(target,0)]
        seen = [target]
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.pop(0)
            for neighbor in [node.left,node.right,node.par]:
                if neighbor and neighbor not in seen:
                    seen.append(neighbor)
                    queue.append((neighbor,d+1))
        return []
