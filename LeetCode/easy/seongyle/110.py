# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cash = {}
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root: Optional[TreeNode]):
            if not root:
                return 0
            if (root in self.cash):
                return self.cash[root]
            self.cash[root] = max(getDepth(root.left), getDepth(root.right)) + 1
            return self.cash[root]
        if not root:
            return True
        return abs(getDepth(root.left) - getDepth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)