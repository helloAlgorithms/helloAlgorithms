class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        index = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]  
                index = index + 1       
        return index
