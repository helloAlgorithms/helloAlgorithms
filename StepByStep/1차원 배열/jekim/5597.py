
def solution(students, attend) -> list:
    ans = []
    for i in range(28):
        attend[int(input())-1] = 1
    for i in range(30):
        if attend[i] == 0:
            ans.append(i+1)
    ans.sort()
    return ans

def runtime() -> None:
    students = range(1, 31)
    attend = [0] * 30
    ans = solution(students, attend)
    print(ans[0])
    print(ans[1])

runtime()