# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        output = []
        q = []
        q.append(root)
        temp = [root.val]
        while q:
            o = []
            output.append(sum(temp)/len(temp))
            for i in range(len(q)):
                t = q.pop(0)
                temp.pop(0)
                if t.left:
                    q.append(t.left)
                    temp.append(t.left.val)
                if t.right:
                    q.append(t.right)
                    temp.append(t.right.val)
        return output
