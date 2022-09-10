import sys

class MelonGrove:
    def __init__(self, borders : list):
        self.borders = borders # list of [x, y], x is direction, y is length
        max_width = 0
        max_height = 0
        max_width_idx = 0
        max_height_idx = 0
        for i in range(len(borders)):
            if borders[i][0] == 1 or borders[i][0] == 2:
                if borders[i][1] > max_width:
                    max_width = borders[i][1]
                    max_width_idx = i
            else:
                if borders[i][1] > max_height:
                    max_height = borders[i][1]
                    max_height_idx = i

        min_width = abs(borders[(max_width_idx-1) % 6][1] - borders[(max_width_idx+1) % 6][1])
        min_height = abs(borders[(max_height_idx-1) % 6][1] - borders[(max_height_idx+1) % 6][1])
        self.area = (max_height*max_width) - (min_height * min_width)

def solution(borders : list, melon : int) -> int:
    melonGrove = MelonGrove(borders)
    return melonGrove.area * melon

def runtime() -> None:
    melon_cnt_in_a_area = int(sys.stdin.readline())
    borders = []
    for i in range(6):
        direction, length = map(int, sys.stdin.readline().split())
        borders.append([direction, length])
    print(solution(borders, melon_cnt_in_a_area))
        
runtime()