class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        swiper = []
        swiper.append(intervals[0])
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a <= swiper[-1][1]:
                c, d = swiper.pop()
                a, b = c, max(b, d)
            swiper.append([a, b])
        return swiper