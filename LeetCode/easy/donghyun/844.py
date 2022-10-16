class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list, t_list = [], []
        for i in s:
            if i == "#":
                if s_list:
                    s_list.pop()
            else:
                s_list.append(i)
        for i in t:
            if i == "#":
                if t_list:
                    t_list.pop()
            else:
                t_list.append(i)
        print(s_list , t_list)
        return s_list == t_list