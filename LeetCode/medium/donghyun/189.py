class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = len(nums) - k % len(nums)
        nums[:] = nums[k:] + nums[:k]