class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess