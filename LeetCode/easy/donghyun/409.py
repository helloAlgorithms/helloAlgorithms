class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        count = 0
        mid = False
        for k, v in d.items():
            if v % 2:
                mid = True
            count += v // 2
        return count * 2 + mid