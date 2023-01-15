class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            res.append(res[i >> 1] + i % 2)
        return res