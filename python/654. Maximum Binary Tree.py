# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums) == 0:
            return
        max_ind = 0
        max_num = 0
        for  i in range(len(nums)):
            if nums[i] > max_num:
                max_num,max_ind = nums[i],i
        
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_ind])
        root.right = self.constructMaximumBinaryTree(nums[max_ind+1:])
        return root
