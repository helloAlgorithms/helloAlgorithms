# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursion_invert(root)
        return root
    
    def recursion_invert(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.recursion_invert(root.left)
        self.recursion_invert(root.right)
