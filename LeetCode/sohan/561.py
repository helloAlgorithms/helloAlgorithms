class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum
