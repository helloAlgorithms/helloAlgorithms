class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        charset = set()
        j = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.discard(s[j])
                j += 1
            charset.add(s[i])
            maxlen = max(maxlen, len(charset))
        return maxlen