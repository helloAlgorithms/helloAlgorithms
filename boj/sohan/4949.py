while True:
    brackets = []
    string = input().strip('.')
    if len(string) == 0:
        break
    if string.count('(') != string.count(')') or string.count('[') != string.count(']'):
        print("no")
    else:
        for character in string:
            if character == '[':
                brackets.append('[')
            if character == ']' and len(brackets) != 0:
                if brackets[-1] == '[':
                    brackets.pop()
            if character == '(':
                brackets.append('(')
            if character == ')' and len(brackets) != 0:
                if brackets[-1] == '(':
                    brackets.pop()
        print("yes" if len(brackets) == 0 else "no")
