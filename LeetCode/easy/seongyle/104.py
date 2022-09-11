# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def searchTree(root: Optional[TreeNode], depth: int) -> int:
            if (root is None):
                return depth
            depth += 1
            return max(searchTree(root.left, depth), searchTree(root.right, depth))
        depth = 0
        depth = searchTree(root, depth)
        return depth
            