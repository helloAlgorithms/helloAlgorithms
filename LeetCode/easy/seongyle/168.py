class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n > 0:
            n -= 1
            res += chr((n % 26) + ord('A'))
            n //= 26
        return res[::-1]
            