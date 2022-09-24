# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root: Optional[TreeNode], res: []):
    if root:
        dfs(root.left, res)
        dfs(root.right, res)
        res.append(root.val)
    return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return dfs(root, res)
