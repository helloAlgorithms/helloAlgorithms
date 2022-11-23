class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = deque(nums)
        rotated = 0
        while nums[0] > nums[-1]:
            nums.rotate(-1)
            rotated += 1
        idx = bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return (idx + rotated) % len(nums)
        return -1