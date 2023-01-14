# Title: 유기농 배추
# Link: https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**6)

def visitBaechu(baechu_farm: list, visited: list, row: int, col: int) -> bool:
    if visited[row][col] == 1:
        return False
    visited[row][col] = 1
    for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        next_row = row + row_offset
        next_col = col + col_offset
        if next_row >= 0 and next_row < len(baechu_farm) and next_col >= 0 and next_col < len(baechu_farm[0]):
            if baechu_farm[next_row][next_col] == 1 and visited[next_row][next_col] == 0:
                visitBaechu(baechu_farm, visited, next_row, next_col)
    return True

def solution(baechu_farm: list, farm_width: int, farm_height: int) -> int:
    worm_count = 0
    visited = [[0 for _ in range(farm_width)] for _ in range(farm_height)]
    for row in range(farm_height):
        for col in range(farm_width):
            if baechu_farm[row][col] == 1 and visited[row][col] == 0:
                if visitBaechu(baechu_farm, visited, row, col) == True:
                    worm_count += 1 
    return worm_count

def generateBaechuFarm(width: int, height: int, baechu_count: int) -> list:
    baechu_farm = [[0 for _ in range(width)] for _ in range(height)]
    for _ in range(baechu_count):
        col, row = map(int, input().split())
        baechu_farm[row][col] = 1
    return baechu_farm

def main() -> None:
    answer = []
    test_case_count = int(input())
    for _ in range(test_case_count):
        width, height, baechu_count = map(int, input().split())
        baechu_farm = generateBaechuFarm(width, height, baechu_count)
        answer.append(solution(baechu_farm, width, height))
    for _ in answer:
        print(_)
    return ;

if __name__ == "__main__":
    main()