class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dic = {')':'(', '}':'{', ']':'['}
        for p in s:
            if p in dic.values():
                stack.append(p)
            elif p in dic.keys():
                if len(stack) == 0 : return False
                if stack.pop() != dic[p]:
                    return False
        if len(stack):
            return False
        return True