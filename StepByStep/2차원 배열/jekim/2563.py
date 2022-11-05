class Paper:
    def __init__(self, x, y):
        self.distance_from_y_axis = x
        self.distance_from_x_axis = y
        self.width = 10
        self.height = 10
    

def solution(papers : list, papers_len : int) -> int:
    area = [[0 for i in range(100)] for j in range(100)]
    cnt = 0
    for i in range(papers_len):
        for j in range(papers[i].distance_from_x_axis, papers[i].distance_from_x_axis + papers[i].width):
            for k in range(papers[i].distance_from_y_axis, papers[i].distance_from_y_axis + papers[i].height):
                if area[j][k] == 0:
                    area[j][k] = 1
                    cnt += 1
    return cnt

def runtime() -> None:
    N = int(input())
    papers = []
    for i in range(N):
        x, y = map(int, input().split())
        papers.append(Paper(x, y))
    area = solution(papers, len(papers))
    print(area)

runtime()