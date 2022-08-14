import sys

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self) -> list:
        return [self.x, self.y]

class Harkey_Ground:
    def __init__(self, width : int, height : int, start_x : int, start_y : int):
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y

    def __is_inside_central_squere(self, player : Player) -> bool:
        x, y = player.get_position()
        return (self.start_x <= x <= self.start_x + self.width) and (self.start_y <= y <= self.start_y + self.height)

    def __is_inside_side_circle(self, player : Player) -> bool:
        x, y = player.get_position()
        radius = self.height / 2
        left_circle_central_x = self.start_x
        left_circle_central_y = self.start_y + radius
        right_circle_central_x = self.start_x + self.width
        right_circle_central_y = self.start_y + radius
        if (x - left_circle_central_x) ** 2 + (y - left_circle_central_y) ** 2 <= radius ** 2:
            return True
        elif (x - right_circle_central_x) ** 2 + (y - right_circle_central_y) ** 2 <= radius ** 2:
            return True
        else: return False 

    def is_player_in_ground(self, player : Player) -> bool:
        return True if self.__is_inside_central_squere(player) or self.__is_inside_side_circle(player) else False


def solution(ground : Harkey_Ground, player_list : list, player_list_len : int) -> int:
    answer = 0
    for i in range(player_list_len):
        if ground.is_player_in_ground(player_list[i]): answer += 1
    return answer

def runtime() -> None:
    width, height, start_x, start_y, player_cnt = map(int, sys.stdin.readline().split())
    harkey_ground = Harkey_Ground(width, height, start_x, start_y)
    player_list = []
    for i in range(player_cnt):
        x, y = map(int, sys.stdin.readline().split())
        player_list.append(Player(x, y))
    print(solution(harkey_ground, player_list, player_cnt))

runtime()