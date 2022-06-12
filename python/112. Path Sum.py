# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum = targetSum - root.val
        if targetSum == 0 and root.left is None and root.right is None:
            return True
        else:
            isleft =  self.hasPathSum(root.left, targetSum)
            if isleft:
                return True
            isright = self.hasPathSum(root.right, targetSum)
            if isright:
                return True
        return False

