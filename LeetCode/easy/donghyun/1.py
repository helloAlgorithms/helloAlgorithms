class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = defaultdict(list)
        for i, num in enumerate(nums):
            idx_dict[num].append(i)
            if idx_dict[target-num]:
                if num == target-num:
                    if len(idx_dict[target-num]) == 2:
                        return idx_dict[target-num]
                    else:
                        continue
                return [idx_dict[num][0], idx_dict[target-num][0]]