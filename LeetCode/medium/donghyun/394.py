class Solution:    
    def decodeString(self, s: str) -> str:
        string = []
        repeats = []
        brackets = []
        chars = defaultdict(list)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                repeat = 0
                while s[i].isdigit():
                    repeat = repeat * 10 + int(s[i])
                    i += 1
                repeats.append(repeat)
                continue
            elif s[i] == "[":
                brackets.append(i)
            elif s[i] == "]":
                j = brackets.pop()
                repeat = repeats.pop()
                for _ in range(repeat):
                    if brackets:
                        chars[brackets[-1]].extend(chars[j])
                    else:
                        string.extend(chars[j])
            else:
                if brackets:
                    chars[brackets[-1]].append(s[i])
                else:
                    string.append(s[i])
            i += 1
        return "".join(string)