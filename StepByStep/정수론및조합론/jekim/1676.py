
def solution(x : int) -> int:
    answer = 0;
    fact = 1
    if x > 1:
        for i in range(2, x+1): fact *= i
    while True:
        if fact % 10 == 0:
            answer += 1
            fact //= 10
        else:
            break
    return answer

def runtime() -> None:
    x = int(input())
    print(solution(x))

runtime()