import sys

class point:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

class circle:
    def __init__(self, x : int, y : int, r : int):
        self.x = x
        self.y = y
        self.r = r
    
    def get_distance_to_point(self, p : point) -> int:
        return (p.x - self.x) ** 2 + (p.y - self.y) ** 2


def solution(coordinate_list : list, circle_coor_list : list, circle_list_len : int) -> int:
    answer = 0
    start_point = point(coordinate_list[0], coordinate_list[1])
    destination_point = point(coordinate_list[2], coordinate_list[3])
    circle_list = []
    for i in range(circle_list_len):
        tmp = circle(circle_coor_list[i][0], circle_coor_list[i][1], circle_coor_list[i][2])
        circle_list.append(tmp)
    
    for i in range(circle_list_len):
        dis1 = circle_list[i].get_distance_to_point(start_point)
        dis2 = circle_list[i].get_distance_to_point(destination_point)
        pow_cr = circle_list[i].r ** 2

        if pow_cr > dis1 and pow_cr > dis2:
            pass
        elif pow_cr > dis1 or pow_cr > dis2:
            answer += 1
    return answer

def runtime() -> None:
    case_cnt = int(sys.stdin.readline())
    for i in range(case_cnt):
        coordinate_list = list(map(int, sys.stdin.readline().split()))
        circle_list_len = int(sys.stdin.readline())
        circle_coordinate_list = []
        for j in range(circle_list_len):
            circle_coordinate_list.append(list(map(int, sys.stdin.readline().split())))
        print(solution(coordinate_list, circle_coordinate_list, circle_list_len))

runtime()