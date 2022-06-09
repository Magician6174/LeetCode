# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return
        s1, s2 = [], []
        output = []
        s1.append(root)
        level = 1
        while s1 or s2:
            l = []
            while s1 and level%2 != 0:
                top = s1.pop()
                l.append(top.val)
                if top.left:
                    s2.append(top.left)
                if top.right:
                    s2.append(top.right)
            while s2 and level%2==0:
                top = s2.pop()
                l.append(top.val)
                if top.right:
                    s1.append(top.right)
                if top.left:
                    s1.append(top.left)
            output.append(l)
            level += 1
        return output
