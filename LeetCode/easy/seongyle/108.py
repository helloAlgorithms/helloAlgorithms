# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums)
        return self.makeBST(start, end, nums)
    def makeBST(self, start: int, end: int, nums: List[int]) -> Optional[TreeNode]:
        if (start >= end):
            return None
        root = TreeNode(nums[(start + end) // 2])
        root.left = self.makeBST(start, (start + end) // 2,  nums)
        root.right = self.makeBST((start + end) // 2 + 1, end, nums)
        return root