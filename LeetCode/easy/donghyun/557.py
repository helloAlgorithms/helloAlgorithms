class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s[::-1].split()[::-1])