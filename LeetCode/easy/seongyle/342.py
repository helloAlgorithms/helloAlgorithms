class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        return n % 4 == 0 and self.isPowerOfFour(n // 4)

# 로그를 이용한 풀이
def isPowerOfFour(self, n: int) -> bool:
    return n > 0 and log(n, 4).is_integer()