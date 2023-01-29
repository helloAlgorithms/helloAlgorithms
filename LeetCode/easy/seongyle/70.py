class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n == 1:
                return 1
            if n == 2: 
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)