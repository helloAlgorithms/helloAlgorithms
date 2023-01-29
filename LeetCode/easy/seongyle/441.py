class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (-1 + int(math.sqrt(1+8*n))) // 2
		