class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if idx == len(nums):
            return -1
        return idx if nums[idx] == target else -1