try:
    T = int(input())
    for i in range(0, T):
        string = input()
        print(string[0], end='')
        print(string.strip()[-1])
except:
    pass
