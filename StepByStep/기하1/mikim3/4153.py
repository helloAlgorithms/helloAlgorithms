# 11:37 시작 11:44끝

a, b, c = map(int,input().split())

while a+b+c > 0:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2+c**2 == a**2:
        print("right")
    else:
        print("wrong")

    a, b, c = map(int,input().split())

