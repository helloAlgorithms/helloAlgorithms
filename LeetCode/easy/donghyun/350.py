class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        count = defaultdict(int)
        for i in nums2:
            count[i] += 1
        l = []
        for i in nums1:
            if count[i]:
                l.append(i)
                count[i] -= 1
        return l