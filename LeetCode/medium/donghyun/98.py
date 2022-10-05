# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(node, min, max):
            if not node:
                return True
            if not (min < node.val < max):
                return False
            return traversal(node.left, min, node.val) and traversal(node.right, node.val, max)
        return traversal(root, -inf, inf)