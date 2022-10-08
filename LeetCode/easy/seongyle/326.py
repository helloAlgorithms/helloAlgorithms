class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        return n % 3 == 0 and self.isPowerOfThree(n // 3)

# 로그변환을 이용한 풀이
def isPowerOfThree(self, n: int) -> bool:
	return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0

# 3^n 최대값을 이용한 풀이
def isPowerOfThree(self, n: int) -> bool:
	return (n > 0) and 1162261467 % n == 0