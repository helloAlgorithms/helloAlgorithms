# Title: 모든 순열
# Link: https://www.acmicpc.net/problem/10974
def dfs(numbers: list, visited: list, answer: list, bucket:list, limit: int, count: int) -> None:
    if len(bucket) == limit:
        answer.append(bucket[:])
        return
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            bucket.append(numbers[i])
            dfs(numbers, visited, answer, bucket, limit, count + 1)
            bucket.pop()
            visited[i] = False
    return

def solution(N: int) -> list:
    numbers = [i for i in range(1, N + 1)]
    visited = [False for _ in range(N)]    
    answer = []
    dfs(numbers, visited, answer, [], N, 0)
    return answer

def printAnswer(answers: list) -> None:
    for _ in answers:
        print(" ".join(map(str, _)))
    return

def main() -> None:
    N = int(input())
    answers = solution(N)
    printAnswer(answers)
    return

if __name__ == "__main__":
    main()
