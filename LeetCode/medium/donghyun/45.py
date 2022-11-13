class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 1
        remained_step = nums[0]
        chage_step = 0
        goal = len(nums) - 1
        if remained_step >= goal:
            return count
        for i in range(1, len(nums)):
            if i == goal:
                return count
            if i + nums[i] >= goal:
                return count + 1
            remained_step -= 1
            chage_step -= 1
            if remained_step < nums[i]:
                chage_step = max(chage_step, nums[i])
            if remained_step == 0:
                count += 1
                remained_step = chage_step