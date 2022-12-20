L = int(input())
string = input()
result = 0
for i, character in enumerate(string):
    result += (ord(character) - 96) * (31 ** i)
print(result % 1234567891)
