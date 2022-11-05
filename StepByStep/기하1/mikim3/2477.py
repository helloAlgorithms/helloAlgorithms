# 시작시간 10:45

# 1,2는 가로길이 3,4 는 세로길이 

from re import sub


melon = int(input())
arr = [list(map(int,input().split())) for _ in range(6)]

# 가장 긴 가로변 길이, 인덱스 초기화
w,w_index = 0,0
h,h_index = 0,0

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2: #가로방향
        if w< arr[i][1]:
            w= arr[i][1]
            w_index = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if h<arr[i][1]:
            h = arr[i][1]
            h_index = i
# print(w,h)
# 작은 사각형의 가로세로
subW= abs(arr[(w_index - 1) % 6][1] - arr[(w_index + 1) % 6][1])
subH= abs(arr[(h_index - 1) % 6][1] - arr[(h_index + 1) % 6][1])
# print(subW,subH)

ans = ((w*h) -(subW*subH)) * melon
print(ans)