class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            sums = sum([int(digits)**2 for digits in str(n)])
            if (sums in seen):
                return False
            n = sums
            seen.add(n)
        return True
        