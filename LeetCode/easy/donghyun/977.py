class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted((i ** 2 for i in nums))