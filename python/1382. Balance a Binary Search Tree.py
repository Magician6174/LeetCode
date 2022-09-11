# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.arr = []
        self.inorder(root)
        
        root = self.buildBalancedBST(None,self.arr)
        
        return root
        
        
        
    def buildBalancedBST(self,root,nums):
        
        nums = list(nums)
        # print(nums)
        n = len(nums)
        if n == 0:
            return
        if root is None:
            root = TreeNode(nums[n//2])
            root.left = self.buildBalancedBST(root,nums[:n//2])
            # print("--->",nums,nums[n//2+1:])
            root.right = self.buildBalancedBST(root,nums[n//2+1:])
        else:
            val = nums[n//2]
            if val < root.val:
                root.left = TreeNode(val)
                root.left.left = self.buildBalancedBST(root.left,nums[:n//2])
                root.left.right = self.buildBalancedBST(root.left,nums[n//2+1:])
                
                return root.left
            else:
                root.right = TreeNode(val)
                root.right.left = self.buildBalancedBST(root.right,nums[:n//2])
                root.right.right = self.buildBalancedBST(root.right,nums[n//2+1:])
                return root.right
            
        return root
        
        
            
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
