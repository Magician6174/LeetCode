# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.hashmap = defaultdict(list)
        self.verticalOrder(root,0,0)
        # print(self.hashmap)
        ans = []
        for i in range(min(self.hashmap),max(self.hashmap)+1):
            ans.append(self.hashmap[i])
        # print(ans)
        for i in range(len(ans)):
            ans[i] = sorted(ans[i],key=lambda l: (l[1],l[0]))
        finalans = []
            
        for i in range(len(ans)):
            temp = []
            for j in range(len(ans[i])):
                temp.append(ans[i][j][0])
            finalans.append(temp)
        return finalans
        
    def verticalOrder(self, root, dist,hdist):
        
        if root is None:
            return
        self.hashmap[dist].append((root.val,dist+hdist))
        self.verticalOrder(root.left,dist-1,hdist+1)
        self.verticalOrder(root.right,dist+1,hdist+1)
        
        
        
        
        
        
        
        
        
        
        
#         self.annotate_nodes(root,[0,0])
#         self.d = defaultdict(list)
#         self.printrc(root)
#         # print(min(self.d),max(self.d)+1)
#         ans = []
#         for i in range(min(self.d),max(self.d)+1):
#             ans.append(sorted(self.d[i]))
#         return ans
        
#     def annotate_nodes(self,root,rc):
#         if root is None:
#             return
#         root.RC = rc
#         self.annotate_nodes(root.left,[rc[0]+1,rc[1]-1])
#         self.annotate_nodes(root.right,[rc[0]+1,rc[1]+1])
    
#     def printrc(self,root):
#         if root is None:
#             return
        
#         self.d[root.RC[1]].append(root.val)
            
#         self.printrc(root.left)
#         self.printrc(root.right)
