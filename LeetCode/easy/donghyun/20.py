class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d['('] = ')'
        d['{'] = '}'
        d['['] = ']'
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if not len(stack) or d[stack.pop()] != i:
                    return False
        return False if len(stack) else True