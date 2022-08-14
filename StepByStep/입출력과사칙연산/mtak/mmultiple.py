_input = []
for i in range(0,2):
    _input.append(int(input()))
result = []
tmp1 = _input[1]
for i in range(0, len(str(_input[1]))):
    tmp = tmp1 % 10
    tmp1 = tmp1 // 10
    result.append(_input[0] * tmp)
    print(result[len(result) - 1])
_return = 0
for i in range(0, len(str(_input[1]))):
    _return += result[i] * 10**i
print(_return)