class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i, num in enumerate(nums):
            if num:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1