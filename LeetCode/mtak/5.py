class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindromic(st):
             return st == st[::-1]
        ret = ''
        s_len = len(s)
        for start in range(s_len):
            for l in range(s_len - start + 1, 1, -1):
                target = s[start: start + l]
                if l <= len(ret): break
                if is_palindromic(target):
                    ret = target if len(target) > len(ret) else ret
        return ret
        
        
