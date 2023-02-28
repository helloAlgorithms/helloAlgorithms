def solution(nums):
    answer = 0
    nums_l = len(nums) // 2
    set_l = len(set(nums))
    answer = nums_l if nums_l <= set_l else set_l
    return answer