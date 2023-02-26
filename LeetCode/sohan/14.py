class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while True:
                try:
                    a = strs[i].index(prefix)
                    if a == 0:
                        break
                except:
                    pass
                prefix = prefix[0:len(prefix) - 1]
                if (len(prefix) == 0):
                    return ""     
        return prefix
