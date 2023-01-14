class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area_cal(corr1, corr2, corr3):
            (x1, y1), (x2, y2), (x3, y3) = corr1, corr2, corr3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return max(area_cal(corr1, corr2, corr3) for corr1, corr2, corr3 in combinations(points, 3))

# 파이썬 itertools를 잘 이용하자
# https://itholic.github.io/python-combination-permutation/