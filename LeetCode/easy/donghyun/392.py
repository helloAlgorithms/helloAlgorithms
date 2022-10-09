class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            i += 1 if s[i] == t[j] else 0
            j += 1
        return i == len(s)