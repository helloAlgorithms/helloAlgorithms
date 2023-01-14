# Title: 날짜 계산
# Link: https://www.acmicpc.net/problem/1476
def solution(earth: int, sun: int, moon: int) -> int:
    year = 1
    while True:
        if (year - earth) % 15 == 0 and (year - sun) % 28 == 0 and (year - moon) % 19 == 0:
            break
        year += 1
    return year

def main() -> None:
    earth, sun, moon = map(int, input().split())
    print(solution(earth, sun, moon))
    return

if __name__ == "__main__":
    main()