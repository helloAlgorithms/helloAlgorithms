# Title: 약수 구하기
# Link: https://www.acmicpc.net/problem/2501
def solution(N: int, K: int) -> int:
    divisors = [i for i in range(1, N + 1) if N % i == 0]
    return divisors[K - 1] if len(divisors) >= K else 0

def main() -> None:
    N, K = map(int, input().split())
    print(solution(N, K))
    return

if __name__ == "__main__":
    main()


