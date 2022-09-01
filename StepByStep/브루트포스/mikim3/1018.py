# 10:41시작 

# 내가 오래걸린 이유  (x + y) % 2 == 0 일때 대각선과 두칸씩 떨어진 위치라는 것을 생각해내지 못해서 코드가 복잡해졌다.
# 체스판 처음이 W 면 WBWB... 으로 해야지만 가장 효율 적이고
# 체스판 처음이 B 면 BWBW... 이 가장 효율적 인줄 알있지만
# "예를 들어 첫 줄이  WWBWBWBW처럼 칠해져 있으면, WBWBWBWB보단 BWBWBWBW로 칠하는 게 효율적입니다."
# 이런경우도 있는걸 몰랐다.



# 아무곳에서나 시작해서 8X8크기의 BW무늬의 체스판을 그리는문제



h,w = map(int,input().split())
li = []
for i in range(h):
    li.append(input())
min_v = 99999
# i , j로 체스판 시작점을 하나씩 옮김
for i in range(0, h-8+1):
    for j in range(0, w-8+1):
        check = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (x+y)%2 == 0:  #  B의 대각선과 그 대각선에서 x 방향으로 두칸씩 떨어진 곳은 전부B이여야만 함
                    if li[y][x] == 'W':
                        check += 1
                else:
                    if li[y][x] == 'B':
                        check += 1
        if check <= min_v:
            min_v = check
        check = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (x+y)%2 == 0:  #  B의 대각선과 그 대각선에서 x 방향으로 두칸씩 떨어진 곳은 전부B이여야만 함
                    if li[y][x] == 'B':
                        check += 1
                else:
                    if li[y][x] == 'W':
                        check += 1
        if check <= min_v:
            min_v = check
print(min_v)







