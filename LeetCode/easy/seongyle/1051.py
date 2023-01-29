class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights)
        i = 0
        cnt = 0
        while (i < len(heights)):
            if heights[i] != ordered[i]:
                cnt += 1
            i += 1
        return cnt