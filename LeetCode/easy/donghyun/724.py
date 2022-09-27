class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        accum = 0
        for i in range(len(nums)):
            if accum << 1 == s - nums[i]:
                return i
            accum += nums[i]
        return -1