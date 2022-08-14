class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        haystackLen = len(haystack)
        i = 0
        
        if (needleLen == 0):
            return (0);
        while (i < haystackLen - needleLen + 1):
            print(haystack[i:i+needleLen])
            if (haystack[i:i+needleLen] == needle):
                return (i)
            i+=1
        return (-1);
        