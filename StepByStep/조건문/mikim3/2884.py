h,m=list(map(int,input().split()))
if m-45<0:  # 분이 빼면 음수가 될때
    m=60+m-45
    if h-1<0:
        h=23
    else:
        h-=1
else:  # 분이 음수 안될때
    m-=45
print(h,m)