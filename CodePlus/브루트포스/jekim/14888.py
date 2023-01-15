# Title: 연산자 끼워넣기
# Link: https://www.acmicpc.net/problem/14888
def cpp14_div(a, b):
    return a // b if a * b > 0 else -(-a // b)

max_value = -1e9
min_value = 1e9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    op = list(map(int, input().split()))

    dfs(1, A[0], op, A, N)
    print(max_value)
    print(min_value)
    return

def dfs(index, result, op, A, N):
    global max_value, min_value
    if index == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        for i in range(4):
            if op[i] > 0:
                op[i] -= 1
                if i == 0:
                    dfs(index + 1, result + A[index], op, A, N)
                elif i == 1:
                    dfs(index + 1, result - A[index], op, A, N)
                elif i == 2:
                    dfs(index + 1, result * A[index], op, A, N)
                else:
                    dfs(index + 1, cpp14_div(result, A[index]), op, A, N)
                op[i] += 1

if __name__ == "__main__":
    main()