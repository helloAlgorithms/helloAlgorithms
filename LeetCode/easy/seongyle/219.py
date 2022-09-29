class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}
        
        for idx, value in enumerate(nums):
            if value in checked and idx - checked[value] <= k:
                return True
            checked[value] = idx;
        return False
