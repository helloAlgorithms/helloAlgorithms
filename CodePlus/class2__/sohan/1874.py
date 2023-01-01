import sys
N = int(input())
series = [int(sys.stdin.readline().strip()) for i in range(N)]
stack = [i+1 for i in range(N)]
stack = stack[::-1]
series = series[::-1]
new_stack = []
result = []
operations = ""

while True:
    if len(series) == 0:
        break
    value = series.pop()
    while (len(stack) != 0 and stack[-1] <= value):
        new_stack.append(stack.pop())
        operations += "+\n"
    next_value = new_stack.pop()
    if (next_value > value):
        print("NO")
        exit(0)
    result.append(next_value)
    operations += "-\n"
print(operations, end='')
