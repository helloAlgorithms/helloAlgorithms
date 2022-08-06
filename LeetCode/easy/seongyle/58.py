class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1;
        flag = 0;
        rtn = 0;
        
        while (i >= 0):
            if (s[i] != ' '):
                flag = 1
                rtn += 1
            if (flag == 1 and s[i] == ' '):
                break
            i -= 1
        return (rtn)
