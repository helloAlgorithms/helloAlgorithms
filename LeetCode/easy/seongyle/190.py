class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:].zfill(32)
        return int(num[::-1], 2)