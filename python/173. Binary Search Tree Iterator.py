# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.current = root
        self.stack = [root]
        self.hn = True

    def next(self) -> int:
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left

        temp = self.stack.pop()
        if temp.right:
            self.current = temp.right
        return temp.val


    def hasNext(self) -> bool:
        if len(self.stack)==1 and self.current is None:
            return False
        return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
