# Title: 일곱 난쟁이
# Link: https://www.acmicpc.net/problem/2309
def solution(dwarf_heights: list) -> list:
    dwarf_heights.sort()
    for i in range(9):
        for j in range(i + 1, 9):
            if sum(dwarf_heights) - dwarf_heights[i] - dwarf_heights[j] == 100:
                return dwarf_heights[:i] + dwarf_heights[i + 1:j] + dwarf_heights[j + 1:]
    return []

def get_dwarf_heights() -> list:
    heights = []
    for _ in range(9):
        heights.append(int(input()))
    return heights

def main() -> None:
    dwarf_heights = get_dwarf_heights()
    answer = solution(dwarf_heights)
    for _ in answer:
        print(_)
    return

if __name__ == "__main__":
    main()