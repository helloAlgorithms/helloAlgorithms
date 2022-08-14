
def get_gcd(a : int, b : int) -> int: return a if b == 0 else get_gcd(b, a % b)

def solution(circle_radius_list : list) -> list:
    answer = []
    for i in range(len(circle_radius_list)):
        gcd = get_gcd(circle_radius_list[0], circle_radius_list[i])
        x = circle_radius_list[0] // gcd
        y = circle_radius_list[i] // gcd
        answer.append("%d/%d" % (x, y))
    answer.pop(0)
    return answer

def print_answer_list(answer_list: list) -> None:
    for answer in answer_list: print(answer)

def runtime() -> None:
    circle_cnt = int(input())
    circle_radius_list = list(map(int, input().split()))
    print_answer_list(solution(circle_radius_list))

runtime()