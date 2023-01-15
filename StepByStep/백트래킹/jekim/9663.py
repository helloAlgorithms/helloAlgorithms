def check(board: list, i: int) -> bool:
    for j in range(i):
        if board[i] == board[j] or abs(board[i] - board[j]) == i - j:
            return False
    return True

def nqueen(board, i, N):
    global count
    if i == N:
        count += 1
        return
    for j in range(N):
        board[i] = j
        if check(board, i):
            nqueen(board, i+1, N)

def solution(board: list, N: int) -> int:
    global count
    count = 0
    nqueen(board, 0, N)
    return count

def runtime() -> None:
    N = int(input())
    board = [0 for i in range(15)]
    ans = solution(board, N)
    print(ans)

if __name__ == "__main__":
    runtime()

# 시간초과 이슈로 인해 C++로 풀이
# 이후 파이썬으로 포팅
# #include <vector>
# #include <iostream>

# int ans;

# bool is_valid(std::vector<int> &vec, int idx, int N) {
#     for (int i = 0; i < idx; i++) {
#         if (vec[idx] == vec[i] || idx - i == abs(vec[idx] - vec[i])) {
#             return false;
#         }
#     }
#     return true;
# }

# void nqueen(std::vector<int> &vec, int idx, int N) {
#     if (idx == N) {
#         ans++;
#         return;
#     }
#     for (int i = 0; i < N; i++) {
#         vec[idx] = i;
#         if (is_valid(vec, idx, N))
#             nqueen(vec, idx + 1, N);
#     }
# }

# int main(void) {
#     int N;
#     std::cin >> N;
#     std::vector<int> vec(N, 0);
#     nqueen(vec, 0, N);
#     std::cout << ans << std::endl;
#     return 0;
# }