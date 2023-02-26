class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            tmp = list()
            for p in s[i:]:
                if p in tmp:
                    break    
                tmp.append(p)
            l = max(l, len(tmp))
        return l

