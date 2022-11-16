class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[len(nums) - 1]
        return nums[len(nums) - 3]
