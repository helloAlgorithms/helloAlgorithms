class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remained_step = nums[0]
        for i in range(1, len(nums)):
            if not remained_step:
                return False
            remained_step = max(remained_step - 1, nums[i])
        return True