class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dic = {')':'(', '}':'{', ']':'['}
        for p in s:
            if p in dic.values():
                stack.append(p)
            elif p in dic.keys():
                if stack.pop() != dic[p]:
                    return False
        return True
