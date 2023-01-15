class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0);
        pos = len(nums) - bisect_right(nums, 0);
        return max(neg, pos);