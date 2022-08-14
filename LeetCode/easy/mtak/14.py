from typing import List

class Solution:
    def getMinPart(self, strs: List[str]) ->str:
        ret = strs[0]
        for p in strs[1:]:
            if (len(ret) > len(p)):
                ret = p
        return ret
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        for i, p in enumerate(self.getMinPart(strs)):
            flag = True
            for it in strs:
                if it[i] != p:
                    flag = False
                    break
            if flag == False:
                break
            ret += p
        return ret

s = Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))