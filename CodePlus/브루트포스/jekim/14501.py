# Title: 퇴사
# Link: https://www.acmicpc.net/problem/14501
day = 0
salary = 1

def solution(meeting_times: list, N: int) -> int:
    dp_table = [0 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        if meeting_times[i][day] + i > N:
            dp_table[i] = dp_table[i + 1]
        else:
            dp_table[i] = max(dp_table[i + 1], dp_table[i + meeting_times[i][day]] + meeting_times[i][salary])
    return max(dp_table)

def main():
    N = int (input())
    meeting_times = []
    for _ in range(N):
        meeting_times.append(list(map(int, input().split())))
    print(solution(meeting_times, N))

if __name__ == "__main__":
    main()