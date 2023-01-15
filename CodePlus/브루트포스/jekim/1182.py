# Title: 부분수열의 합
# Link: https://www.acmicpc.net/problem/1182
def solution(numbers: list, S: int, N: int) -> int:
    answer = 0
    for i in range(1, 2 ** N):
        bucket = []
        for j in range(N):
            if i & (1 << j):
                bucket.append(numbers[j])
        if sum(bucket) == S:
            answer += 1
    return answer

def main() -> None:
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solution(numbers, S, N))
    return

if __name__ == "__main__":
    main()
